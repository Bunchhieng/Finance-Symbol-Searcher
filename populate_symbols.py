import csv
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FinanceSymbols.settings')

import django
django.setup()

from symbolsapp.models import Symbol

def populate():
    with open('symbols.csv', 'rU') as sym:
        reader = csv.reader(sym)
        for row in reader:
            add_symbol(str(row[0]), str(row[1]))

    # Print out what we have added to the user.
    for c in Symbol.objects.all():
        print("- {0}").format(str(c))


def add_symbol(symbol, ticker):
    c = Symbol.objects.get_or_create(symbol=symbol, ticker=ticker)
    return c

# Start execution here!
if __name__ == '__main__':
    print("Starting Symbols population script...")
    populate()