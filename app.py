from flask import Flask, render_template, request, url_for, Response
import os
import requests
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get', methods=['GET'])
def get():
    url=request.args['url']
    app_request = requests.get(url)
    return Response(app_request.content, content_type=app_request.headers['Content-Type'])

if __name__ == '__main__':
    app.run()