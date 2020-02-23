from flask_restful import Resource, reqparse
import os
import sqlite3

path = os.getcwd()
corrected_path = path[:-4] + 'data/StocksDB.db'
print(corrected_path)

class StockApi(Resource):
    def __init__(self):
        self.companies = {
            'Walmart': 'WMT',
            'Oracle': 'ORCL',
            'JPMorgan': 'JPM',
            'Visa': 'V',
            'Snap': 'SNAP'
        }

        self.db = sqlite3.connect('StocksDB.db')
        self.c = self.db.cursor()

    def get(self, name, date):
        # Need to check if information is inside of database
        # Grab the dates
        # Return to user

        if name in self.companies:
            ticker_name = self.companies[name]

            if date:
                search_query = """
                    select * from stock where (ticker == ticker_name AND date == date);
                """
            else:
                search_query = """
                    select * from stock where ticker == ticker_name LIMIT 1;
                """

                query = self.c.execute(search_query)
                rows = query.fetchall()

                ans = {}

                for row in rows:
                    ans['ticker'] = row[0]
                    ans['open'] = row[2]
                    ans['close'] = row[3]

                return ans, 200
        else:
            return "Company information not currently tracked", 404
