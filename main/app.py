# flask app
from flask import Flask, render_template, request
import os

app = Flask(__name__)
#Setup base directory for images
app.config["IMAGE_UPLOADS"] = os.path.join('static','uploads')

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/v1/stock/information', methods=['GET'])
def information():

#start flask apps
app.run(debug=True)