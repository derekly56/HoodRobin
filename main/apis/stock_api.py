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

        #self.db = sqlite3.connect(corrected_path)
        #self.c = self.db.cursor()

    def get(self):
        # Need to check if information is inside of database
        # Grab the dates
        # Return to user
        return "Success", 200
        '''
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
        else:
            return "Company information not currently tracked", 404
        '''
