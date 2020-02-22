import sqlite3
import pandas as pd
from pandas import DataFrame
import csv

stock_table = """
                CREATE TABLE IF NOT EXISTS stock (
                ticker text,
                date text,
                open float,
                close float,
                high float,
                low float,
                volume int
            ); """

def create_table():
    conn = sqlite3.connect('StocksDB.db')
    c = conn.cursor()
    c.execute(stock_table)

    with open('jpm.csv','r') as f:

        dr = csv.DictReader(f)
        to_db_jpm = [(i['ticker'], i['date'], i['open'], i['close'], i['high'], i['low'], i['volume']) for i in dr]

    with open('orcl.csv','r') as f:

        dr = csv.DictReader(f)
        to_db_orcl = [(i['ticker'], i['date'], i['open'], i['close'], i['high'], i['low'], i['volume']) for i in dr]

    with open('snap.csv','r') as f:

        dr = csv.DictReader(f)
        to_db_snap = [(i['ticker'], i['date'], i['open'], i['close'], i['high'], i['low'], i['volume']) for i in dr]

    with open('v.csv','r') as f:

        dr = csv.DictReader(f)
        to_db_v = [(i['ticker'], i['date'], i['open'], i['close'], i['high'], i['low'], i['volume']) for i in dr]

    with open('wmt.csv','r') as f:

        dr = csv.DictReader(f)
        to_db_wmt = [(i['ticker'], i['date'], i['open'], i['close'], i['high'], i['low'], i['volume']) for i in dr]

    c.executemany("INSERT INTO stock (ticker, date, open, close, high, low, volume) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db_jpm)
    c.executemany("INSERT INTO stock (ticker, date, open, close, high, low, volume) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db_orcl)
    c.executemany("INSERT INTO stock (ticker, date, open, close, high, low, volume) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db_snap)
    c.executemany("INSERT INTO stock (ticker, date, open, close, high, low, volume) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db_v)
    c.executemany("INSERT INTO stock (ticker, date, open, close, high, low, volume) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db_wmt)
    conn.commit()
    conn.close()

create_table()
