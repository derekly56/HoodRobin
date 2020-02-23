# flask app
from flask import Flask, render_template, request
import os
from apis.stock_api import *

app = Flask(__name__)
#Setup base directory for images
app.config["IMAGE_UPLOADS"] = os.path.join('static','uploads')

@app.route('/')
def homepage():
    return render_template("homepage.html")

# @app.route('/v1/stock/information', methods=['GET'])
# def information():
#     # retrieve URL params
#     name = request.args.get('name', default = 'Walmart', type = str)
#     date = request.args.get('date', default = '2020-02-22', type = str)
#     pass

#start flask apps
app.run(debug=True)