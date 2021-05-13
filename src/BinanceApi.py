import json
import urllib.request

import uno
import unohelper
from com.crypto.api.Binance import XCryptoBinance

class BinanceImpl(unohelper.Base, XCryptoBinance):
    def __init__(self, ctx):
        self.ctx = ctx
    def binancePrice(self, symbol):
        with urllib.request.urlopen("https://api.binance.us/api/v1/ticker/24hr?symbol=" + symbol) as response:
            rawResponse = response.read()
            data = json.loads(rawResponse)
            return data['weightedAvgPrice']

def createInstance(ctx):
    return BinanceImpl(ctx)
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
    createInstance,
    "com.crypto.api.Binance.python.BinanceImpl",
    ("com.sun.star.sheet.AddIn",)
)
