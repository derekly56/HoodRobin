from flask_restful import Resource, reqparse
import os
import sqlite3

path = os.getcwd()
corrected_path = path[:-4] + 'data/StocksDB.db'

companies = {
    'Walmart': 'WMT',
    'Oracle': 'ORCL',
    'JPMorgan': 'JPM',
    'Visa': 'V',
    'Snap': 'SNAP'
}

def get(name, date=""):

    if name in companies:
        db = sqlite3.connect('StocksDB.db')
        cursor = db.cursor()

        ticker_name = companies[name]

        if date:
            search_query = """
                select * from stock where (ticker == ticker_name AND date == date);
            """
        else:
            search_query = """
                select * from stock where ticker == ticker_name LIMIT 1;
            """

            query = cursor.execute(search_query)
            rows = query.fetchall()

            ans = {}

            for row in rows:
                ans['ticker'] = row[0]
                ans['open'] = row[2]
                ans['close'] = row[3]

            return ans, 200
    else:
        return "Company information not currently tracked", 404
