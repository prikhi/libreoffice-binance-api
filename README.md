# LibreOffice Calc - Binance API Extension

This is a simple LibreOffice Calc extension that provides a `BINANCEPRICE` function
for pulling a coin's current average weighted price from Binance's API.

**TODO**: All I need is the average weighted price but maybe exposing the other
fields would be useful to people.

## Build / Install

You need to install `7zip`, `make`, `python`, & the libreoffice-sdk.

Then you can just run `make` to generate `BinanceApi.oxt`.

In LibreOffice, go to `Tools -> Extension Manager -> Add` and select the
`BinanceApi.oxt` file.

## Usage

Simply pass your trading pair to the `BINANCEPRICE` function:

    =BINANCEPRICE("XMRETH")

## LICENSE

GPL-3.0
