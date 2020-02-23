from flask import Flask
from flask_restful import Api
from apis.stock_api import StockApi
import sqlite3
import pandas as pd

app = Flask(__name__)
api = Api(app)

api.add_resource(StockApi, "/v1/stock/information", "/v1/stock/information/<string:name>")

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
