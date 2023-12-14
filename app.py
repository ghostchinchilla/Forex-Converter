from flask import Flask, request, render_template, flash, jsonify, session, redirect
from convert import validate_curr_code 
# from flask_debugtoolbar import DebugToolbarExtension
import requests
from babel import numbers
from convert import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ImASecretKey'

# toolbar = DebugToolbarExtension(app)

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def showHomepage():
    """Display home page with form for client to fill out desired conversion currencies and amount"""

    return render_template('homepage.html')

@app.route('/result')
def showResult():
    """Display the conversion result from user's input, or redirect to the homepage with a flash message telling the user what went wrong"""

    from_curr = request.args.get('from-curr').upper()
    to_curr = request.args.get('to-curr').upper()
    amount = request.args.get('amount')

    if validate_curr_code(from_curr) == 'invalid':
        flash(f'{from_curr} is not a valid currency code.')
        return redirect('/')
    if validate_curr_code(to_curr) == 'invalid':
        flash(f'{to_curr} is not a valid currency code.')
        return redirect('/')

    # url =  f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
    url = f'https://api.exchangerate.host/convert?from={from_curr}&to={to_curr}&amount={amount}'

    resp = requests.get(url)
    data = resp.json()

    result = round(data['result'], 2)

    curr_symbol = numbers.get_currency_symbol(to_curr, 'en_US')

    return render_template('result.html', result=result, curr_symbol=curr_symbol)










# from_curr = str(input("Enter the currency you'd like to convert from:")).upper()

# to_curr = str(input("Enter the currency you'd like to convert to:")).upper()

# amount = float(input("Enter amount to be converted:"))

# response = requests.get(
#     f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
# print(f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")


# Enter the currency you'd like to convert from:usd
# Enter the currency you'd like to convert to:gbp 
# Enter amount to be converter:150                                                                                     
# 150.0 USD is 118.86 GBP  

