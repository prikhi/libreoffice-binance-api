# LibreOffice Calc - Binance API Extension

This is a simple LibreOffice Calc extension that provides a `BINANCEPRICE` function
for pulling a coin's current average weighted price from Binance's API.

**TODO**: All I need is the average weighted price but maybe exposing the other
fields would be useful to people.


## Install

Download the latest plugin from the [Releases page][releases]. Make sure you
grab the `BinanceApi.oxt` and not the source code downloads.

In LibreOffice, go to `Tools -> Extension Manager -> Add` and select the
`BinanceApi.oxt` file you downloaded. Restart LibreOffice when prompted.


## Usage

Simply pass your trading pair to the `BINANCEPRICE` function:

    =BINANCEPRICE("XMRETH")


## Build

If you want to build the plugin yourself, you need to install `7zip`, `make`,
`python`, & the libreoffice-sdk.

Then you can just run `make` to generate `BinanceApi.oxt`.


## LICENSE

GPL-3.0

[releases]: https://github.com/prikhi/libreoffice-binance-api/releases/
