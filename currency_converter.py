from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d558108"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()["results"]
    return list(data.items()).sort()


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - ({symbol})")


def exchange_rates(c1, c2):
    endpoint = f"api/v7/convert?q={c1}_{c2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()
    if len(data) == 0:
        print("No currencies found, probably invalid currency input")
        return
    return list(data.values())[0]


def convert_currencies(c1, c2, amount):
    rate = exchange_rates(c1, c2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return
    converted_amount = amount * rate
    print(f"{amount} {c1} is equal to - {converted_amount} {c2}")


def main():
    currencies = get_currencies()
    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rates of two currencies\n")

    while True:
        command = input("Enter a command or q to quit: ").lower()
        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert_currencies(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            print(f"Result: {exchange_rates(currency1, currency2)}")
        else:
            print("Unrecognized command!")
    print("\nGoodbye! Thanks for use!")


if __name__ == "__main__":
    main()