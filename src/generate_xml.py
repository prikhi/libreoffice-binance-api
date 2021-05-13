# XML generation for Binance API
# Based off of example created by jan@biochemfusion.com April 2009.

addin_id = "com.crypto.api.Binance"
addin_version = "2.0.0"
addin_displayname = "Binance API"
addin_publisher_link = "http://www.github.com/prikhi/libreoffice-binance-api/"
addin_publisher_name = "Pavan Rikhi"

# TODO: Abstract the specifics from below into additional `addin_` variables


# description.xml
#
#

desc_xml = open('description.xml', 'w')

desc_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
desc_xml.write('<description xmlns="http://openoffice.org/extensions/description/2006" \n')
desc_xml.write('xmlns:d="http://openoffice.org/extensions/description/2006" \n')
desc_xml.write('xmlns:xlink="http://www.w3.org/1999/xlink"> \n' + '\n')
desc_xml.write('<dependencies> \n')
desc_xml.write('	<OpenOffice.org-minimal-version value="2.4" d:name="OpenOffice.org 2.4"/> \n')
desc_xml.write('</dependencies> \n')
desc_xml.write('\n')
desc_xml.write('<identifier value="' + addin_id + '" /> \n')
desc_xml.write('<version value="' + addin_version + '" />\n')
desc_xml.write('<display-name><name lang="en">' + addin_displayname + '</name></display-name>\n')
desc_xml.write('<publisher><name xlink:href="' + addin_publisher_link + '" lang="en">' + addin_publisher_name + '</name></publisher>\n')
desc_xml.write('\n')
desc_xml.write('</description> \n')

desc_xml.close

def add_manifest_entry(xml_file, file_type, file_name):
	xml_file.write('<manifest:file-entry manifest:media-type="application/vnd.sun.star.' + file_type + '" \n')
	xml_file.write('	manifest:full-path="' + file_name + '"/> \n')

# manifest.xml
#
# List of files in package and their types.

manifest_xml = open('manifest.xml', 'w')

manifest_xml.write('<manifest:manifest>\n');
add_manifest_entry(manifest_xml, 'uno-typelibrary;type=RDB', 'XBinanceApi.rdb')
add_manifest_entry(manifest_xml, 'configuration-data', 'CalcAddIn.xcu')
add_manifest_entry(manifest_xml, 'uno-component;type=Python', 'BinanceApi.py')
manifest_xml.write('</manifest:manifest> \n')

manifest_xml.close

# CalcAddIn.xcu
#
#

# instance_id references the named UNO component instantiated by Python code (that is my understanding at least).
instance_id = "com.crypto.api.Binance.python.BinanceImpl"
# Name of the corresponding Excel add-in if you want to share documents across OOo and Excel.
excel_addin_name = "BinanceApi.xlam"

def define_function(xml_file, function_name, description, parameters):
	xml_file.write('  <node oor:name="' + function_name + '" oor:op="replace">\n')
	xml_file.write('    <prop oor:name="DisplayName"><value xml:lang="en">' + function_name + '</value></prop>\n')
	xml_file.write('    <prop oor:name="Description"><value xml:lang="en">' + description + '</value></prop>\n')
	xml_file.write('    <prop oor:name="Category"><value>Add-In</value></prop>\n')
	xml_file.write('    <prop oor:name="CompatibilityName"><value xml:lang="en">AutoAddIn.Binance.' + function_name + '</value></prop>\n')
	xml_file.write('    <node oor:name="Parameters">\n')

	for p, desc in parameters:
		# Optional parameters will have a displayname enclosed in square brackets.
		p_name = p.strip("[]")
		xml_file.write('      <node oor:name="' + p_name + '" oor:op="replace">\n')
		xml_file.write('        <prop oor:name="DisplayName"><value xml:lang="en">' + p_name + '</value></prop>\n')
		xml_file.write('        <prop oor:name="Description"><value xml:lang="en">' + desc + '</value></prop>\n')
		xml_file.write('      </node>\n')

	xml_file.write('    </node>\n')
	xml_file.write('  </node>\n')

#
calcaddin_xml = open('CalcAddIn.xcu', 'w')

calcaddin_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
calcaddin_xml.write('<oor:component-data xmlns:oor="http://openoffice.org/2001/registry" xmlns:xs="http://www.w3.org/2001/XMLSchema" oor:name="CalcAddIns" oor:package="org.openoffice.Office">\n')
calcaddin_xml.write('<node oor:name="AddInInfo">\n')
calcaddin_xml.write('<node oor:name="' + instance_id + '" oor:op="replace">\n')
calcaddin_xml.write('<node oor:name="AddInFunctions">\n')

define_function(calcaddin_xml, \
	'binancePrice', 'Retrieve the weighted price for a Binance Ticker', \
	[('symbol', 'The Binance Pair Ticker(e.g., XMRETH)')])

calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</node>\n')
calcaddin_xml.write('</oor:component-data>\n')

calcaddin_xml.close

# Done
