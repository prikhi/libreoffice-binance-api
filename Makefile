LIBRE_LIB=/usr/lib/libreoffice
LIBRE_IDL=/usr/share/idl/libreoffice/

PKG_NAME=BinanceApi
INTERFACE_NAME=X${PKG_NAME}


build: clean src/* idl/*.idl
	${LIBRE_LIB}/sdk/bin/idlc -w -I "${LIBRE_IDL}" "idl/${INTERFACE_NAME}.idl"
	${LIBRE_LIB}/program/regmerge -v "idl/${INTERFACE_NAME}.rdb" /UCR "idl/${INTERFACE_NAME}.urd"
	python src/generate_xml.py
	mkdir -p "${PKG_NAME}/META-INF"
	mv manifest.xml "${PKG_NAME}/META-INF"
	mv description.xml CalcAddIn.xcu "idl/${INTERFACE_NAME}.rdb" "${PKG_NAME}/"
	cp "src/${PKG_NAME}.py" "${PKG_NAME}/"
	cd "${PKG_NAME}"; 7z a -tzip "${PKG_NAME}.oxt" .; mv "${PKG_NAME}.oxt" ..


clean:
	rm -rf ${PKG_NAME}/ ${PKG_NAME}.oxt idl/${INTERFACE_NAME}.rdb idl/${INTERFACE_NAME}.urd
