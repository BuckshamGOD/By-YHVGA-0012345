import requests
import re
import string
import random
import json
import os, sys, time, io,re

                                                                  
bin = input('Enter Bin (6D): ')
print("")
os.system("clear")
binomio = requests.get("https://api-3-ochre.vercel.app/bin="+bin).json()
valid = binomio["status"]
brand = binomio["brand"]
type = binomio["type"]
level = binomio["level"]
bank = binomio["bank"]
phone = binomio["phone"]
country = binomio["country"]
coco = binomio["code"]
flag = binomio["flag"]
currency = binomio["currency"]

b = requests.get("https://api-3-ochre.vercel.app/bin="+bin)
print("==============")

if '"status":true' in b.text:
    print("BIN CHECKER [✓]")
    print("Bin: "+bin)
    print("Valid: "+(str(valid)))
    print("Brand: "+(str(brand)))
    print("Type: "+(str(type)))
    print("Level: "+(str(level)))
    print("Bank: "+(str(bank)))
    print("Phone: "+(str(phone)))
    print("Currency: "+(str(currency)))
    print("Country: "+(str(country))+("("+coco+")")+(str(flag)))

else:
    print("INTERNAL ERROR!")
