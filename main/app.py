# flask app
from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)
#Setup base directory for images
app.config["IMAGE_UPLOADS"] = os.path.join('static','uploads')

companies = {
    'Walmart': 'WMT',
    'Oracle': 'ORCL',
    'JPMorgan': 'JPM',
    'Visa': 'V',
    'Snap': 'SNAP'
}

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/v1/stock/information/highest', methods=['GET'])
def highest():
    # retrieve URL params
    name = request.args.get('name', default = '', type = str)
    path_db = os.getcwd() + '/data/StocksDB.db'

    if not name:
        return 'Error --- Missing Field(s): Name', 404

    if name in companies:
        db = sqlite3.connect(path_db)
        cursor = db.cursor()

        ticker_name = companies[name]

        search_query = """
            select * from stock where ticker == '{0}' order by high DESC LIMIT 3;
        """.format(ticker_name)

        query = cursor.execute(search_query)
        rows = query.fetchall()

        ans = {}

        for row in rows:
            sub_ans = {}
            sub_ans['ticker'] = row[0]
            sub_ans['open'] = row[2]
            sub_ans['close'] = row[3]
            sub_ans['high'] = row[4]
            sub_ans['low'] = row[5]
            sub_ans['volume'] = row[6]

            ans[row[1]] = sub_ans
        return ans, 200

    else:
        return "Company information not currently tracked", 404

@app.route('/v1/stock/information', methods=['GET'])
def information():
    # retrieve URL params
    name = request.args.get('name', default = '', type = str)
    date = request.args.get('date', default = '', type = str)
    path_db = os.getcwd() + '/data/StocksDB.db'

    if not name:
        return 'Error --- Missing Field(s): Name', 404

    if name in companies:
        db = sqlite3.connect(path_db)
        cursor = db.cursor()

        ticker_name = companies[name]

        if date:
            search_query = """
                select * from stock where (ticker == '{0}' AND date == '2020-02-21');
            """.format(ticker_name, date)

            query = cursor.execute(search_query)
            rows = query.fetchall()

            ans = {}

            for row in rows:
                sub_ans = {}

                ans['ticker'] = row[0]
                ans['date'] = row[1]
                ans['open'] = row[2]
                ans['close'] = row[3]
                ans['high'] = row[4]
                ans['low'] = row[5]
                ans['volume'] = row[6]

            return ans, 200

        else:
            search_query = """
                select * from stock where ticker == '{0}' LIMIT 1;
            """.format(ticker_name)

            query = cursor.execute(search_query)
            rows = query.fetchall()

            ans = {}

            for row in rows:
                ans['ticker'] = row[0]
                ans['date'] = row[1]
                ans['open'] = row[2]
                ans['close'] = row[3]
                ans['high'] = row[4]
                ans['low'] = row[5]
                ans['volume'] = row[6]

            return ans, 200
    else:
        return "Company information not currently tracked", 404

#start flask apps
app.run(debug=True)
