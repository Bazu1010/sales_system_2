from flask import Flask,render_template

## to return a html page we use the render_templates

app = Flask (__name__)

## Creating a route
## ("/") shows the starting of a web page before request that doesn't have a name

@app.route("/sana")
def index():
    return render_template("mycarosel.html")

   ## Flask deploys the code


@app.route("/salamu")
def bazu():
    return "Niaje Bazu"

   ## Flask deploy html page


@app.route("/alafu")
def anotherf():
    return render_template("index.html")
app.run()