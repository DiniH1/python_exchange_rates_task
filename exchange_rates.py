from app.exchange_currency import ExchangeCurrency
import json

currency = open("exchange_rates.json", 'r')
currency_dict = json.load()
print(currency_rates)