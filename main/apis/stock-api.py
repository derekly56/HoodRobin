from flask_restful import Resource, reqparse
from stock_data import data

class StockApi(Resource):
    def __init__(self):
        self.stock_datas = data

    def get(self, ticker, date=""):
        # Need to check if information is inside of database
        # Grab the dates
        # Return to user

        if ticker in self.stock_datas:
            response = self.stock_datas[ticker]
            return response, 200
        else:
            return "Could not find Company by that Ticker", 404

    def post(self):
        # TODO:
        pass

    def put(self):
        # TODO:
        pass

    def delete(self):
        # TODO:
        pass
