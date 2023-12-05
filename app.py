import requests

from_currency = str(input("Enter the currency you'd like to convert from:")).upper()

to_currency = str(input("Enter the currency you'd like to convert to:")).upper()

amount = float(input("Enter amount to be converter:"))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")


# Enter the currency you'd like to convert from:usd
# Enter the currency you'd like to convert to:gbp 
# Enter amount to be converter:150                                                                                     
# 150.0 USD is 118.86 GBP  

