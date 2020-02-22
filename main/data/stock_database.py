import sqlite3
import pandas as pd

stock_table = """
                CREATE TABLE IF NOT EXISTS stock (
                ticker text PRIMARY KEY,
                begin_date text,
                end_date text
            ); """

def fix_table(file, ticker):
    add_ticker = ticker + ','
    count = 0
    new_file = open('wmt.csv', 'w')

    with open(file, 'r') as f:
        for cnt, line in enumerate(f):
            if cnt == 0:
                line = 'Ticker' + ',' + line
                new_file.write(line)
            else:
                line = ticker + ',' + line
                new_file.write(line)

    new_file.close()

fix_table('WALMART.csv', 'WMT')
