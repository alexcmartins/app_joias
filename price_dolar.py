import requests


def dolar():
    r = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    data = r.json()
    return {
        'coin': data["USDBRL"]["code"],
        'name': data["USDBRL"]["name"],
        'bid': data["USDBRL"]["bid"],  # Compra
        'ask': data["USDBRL"]["ask"],  # Venda
        'high': data["USDBRL"]["high"],  # Máximo
        'low': data["USDBRL"]["low"]  # Mínimo
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(dolar())
