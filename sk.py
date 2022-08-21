import re
import string
import random
import json
import requests                                                        
import os, sys, time, io,re
#sk checker
skkey = input("Enter Sk!: ")
os.system("clear")
                                                                       
if int(len(skkey)) == 0:
    print("Enter Sk!")



pos = requests.post(f"https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '4543218722787334','card[cvc]': '780','card[exp_month]': '07','card[exp_year]': '2026'}, auth=(skkey, ""))


if 'Invalid API Key provided' in pos.text:
    print("DEAD!")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: Invalid API Key provided")

elif 'rate_limit' in pos.text:
    print("DEAD!")
    print("────────────────────")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: rate_limit")
elif 'api_key_expired' in pos.text:
    print("DEAD!")
    print("────────────────────")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: api_key_expired""")
                                                                       elif 'testmode_charges_only' in pos.text:                                  print("DEAD!")                                                         print("────────────────────")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: testmode_charges_only")

elif 'test_mode_live_card' in pos.text:
    print("DEAD!")
    print("────────────────────")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: test_mode_live_card""")

elif 'Your Card Was Declined' in pos.text:
    print("LIVE! >✅")
    print("────────────────────")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: Sk_Live !")
else:
    print("LIVE! >✅")
    print("────────────────────")
    print("Sk:"+skkey)
    print("────────────────────")
    print("Reason: Sk_Live !")
