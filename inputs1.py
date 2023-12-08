import random
import time
import sys

def forsenadPrint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

def is_valid_integer(input_str):
    return input_str.isdigit()

def start():
    while True:
        val = input("Vill du spela Sigma Souls?\n1. Ja\n2. Nej\n")
        if is_valid_integer(val):
            val = int(val)
            if val == 1:
                forsenadPrint("Du har valt att spela Sigma Souls.")
                break
            elif val == 2:
                forsenadPrint("Du har valt att inte spela Sigma Souls.")
                break
            else:
                forsenadPrint("Ogiltigt input, försök igen...\a")
        else:
            forsenadPrint("Felaktig inmatning, försök igen...\a")

def plot():
    while True:
        vapenval = input("Vad är din val då? \n1. Svärd\n2. Yxa\n3. Hammaren\n")
        if is_valid_integer(vapenval):
            vapenval = int(vapenval)
            if 1 <= vapenval <= 3:
                forsenadPrint(f"Du valde {vapenval}.")
                break
            else:
                forsenadPrint("Ogiltigt val, försök igen...\a")
        else:
            forsenadPrint("Felaktig inmatning, försök igen...\a")

forsenadPrint("Välkommen1\n")
start()
plot()


