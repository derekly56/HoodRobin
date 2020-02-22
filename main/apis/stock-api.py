from flask_restful import Resource, reqparse
import os
import sqlite3

path = os.getcwd()
corrected_path = path[:-4] + 'data/StocksDB.db'

class StockApi(Resource):
    def __init__(self):
        self.companies = {
            'Walmart': 'WMT',
            'Oracle': 'ORCL',
            'JPMorgan': 'JPM',
            'Visa': 'V',
            'Snap': 'SNAP'
        }

        self.db = sqlite3.connect(corrected_path)
        self.c = self.db.cursor()

    def get(self, ticker, date=""):
        # Need to check if information is inside of database
        # Grab the dates
        # Return to user
        pass

    def post(self):
        # TODO:
        pass

    def put(self):
        # TODO:
        pass

    def delete(self):
        # TODO:
        pass
