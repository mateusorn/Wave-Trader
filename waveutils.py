import dotenv
import json
import os
import requests
import time

from binance import Client

from mathutils import convert_percent_to_mul


class WaveEngine:

    def __init__(self, path='settings.json', envpath='.env'):
        self.path = path
        self.PUBKEY = dotenv.dotenv_values(envpath)['PUBLICKEY']
        self.PRIVKEY = dotenv.dotenv_values(envpath)['PRIVKEY']
        self.client = Client(self.PUBKEY, self.PRIVKEY)

        with open(path, 'r') as f:
            self.content = json.load(f)

        self.symbol = self.content['symbol']
        self.sell_ptg = self.content['sell_percentage']
        self.stop_loss = self.content['stop_loss']
        self.sell_multiplier = convert_percent_to_mul(self.sell_ptg, loss=False)
        self.loss_multiplier = convert_percent_to_mul(self.stop_loss)
        self.buy_on_avg = self.content['buy_on_average']

    def get_prices(self):
        ticker_data = self.client.get_ticker(symbol=self.symbol)
        if self.buy_on_avg:
            buy_price = ticker_data['weightedAvgPrice']
            sell_profit = buy_price * self.sell_multiplier
            sell_loss = buy_price * self.loss_multiplier
        else:
            buy_price = float(input("ENTER PRICE >> "))  # Couldn't come up with better solution, gonna change it later.
            sell_profit = buy_price * self.sell_multiplier
            sell_loss = buy_price * self.loss_multiplier
        return sell_profit, sell_loss

    def get_klines(self):
        klines = self.client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")
        days = [time.ctime(x[0]/1000) for x in klines]
        volumes = [x[5] for x in klines]

        return days, volumes





