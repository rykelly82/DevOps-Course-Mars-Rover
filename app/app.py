from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={os.getenv("API_KEY")}&date=2023-03-21')
    result = response.json()
    print(result["url"])
    return render_template('index.html', landing_image=result["url"])

    



@app.route('/mars')
def mars():
    return render_template('mars.html')