# render_template will be used to render the content on the html page with the help of flask
from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])

def index():
    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)

    # getting the html data of the requested url in the soup variable
    soup = BeautifulSoup(req.content,"html.parser")

    # print(soup)
    # print(soup.prettify()) 
    outerdivdata = soup.find_all("div",class_="widget-listing", limit=5)
    # print(outerdivdata) # A collection of 6 divs with a particular class (like a python list)

    headlines = ""
    for data in outerdivdata:
        headline = data.div.div.a["title"]
        headlines += "\u2022 " + headline + "\n\n"
    return render_template("index.html",news=headlines)

