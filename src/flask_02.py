import os

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)

'''


'''
@app.route('/')
def index():
    print("http method:"+request.method)
    # return redirect(url_for("index", "Hello NLP"))
    return render_template("index.html")

if __name__ == '__main__':
    app.run()