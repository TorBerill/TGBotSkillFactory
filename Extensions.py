import requests
import json
from Config import keys


class ConvertionException(Exception):
    pass


class ManyConverter:
    @staticmethod
    def converter(quote: str, base: str,  amount: str):
        if quote == base:
            raise ConvertionException(f"Невозможно перевести схожую валюту {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось опознать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось лпознать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")

        r = requests.get(f"https://data.fixer.io/api/latest/?access_key = YOsdjXzD9lOac53bA2tGc8KHsrWvsXWD&from={quote_ticker}&to={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]

        return total_base