import requests
import json
from config import keys

class APIException(Exception):
    pass

class ExchangeConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Нельзя перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f"https://v6.exchangerate-api.com/v6/fab25befe3413d4a924cba43/pair/{base_ticker}/{quote_ticker}/{amount}"
        )
        total_base = json.loads(r.content)['conversion_result']

        return total_base
