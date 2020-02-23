# flask app
from flask import Flask, render_template, request
import os
from apis.stock_api import StockApi

app = Flask(__name__)
#Setup base directory for images
app.config["IMAGE_UPLOADS"] = os.path.join('static','uploads')

# build connection to back end
api.add_resource(StockApi, "/v1/stock/information")

@app.route('/v1/stock/')
def homepage():
    return render_template("homepage.html")

@app.route('/v1/stock/information')
def get():
    
#start flask apps
app.run(debug=True)