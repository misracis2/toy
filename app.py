import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

from bson import json_util
app = Flask(__name__)


from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.rv3ttod.mongodb.net/test', tlsCAFile=ca)
db = client.hanghae_10_preliminary

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://travel.naver.com/overseas/MV574293953/city/summary',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

@app.route('/')
def home():

    return render_template('toy.html')

@app.route("/travel", methods=["GET"])
def travel_get():
    travel_list = list(db.travel.find({}, {'_id': False}))


    return jsonify({'travel': travel_list})

rest_imgs = soup.select('#NM_NEWSSTAND_DEFAULT_THUMB > div._NM_UI_PAGE_CONTAINER > div:nth-child(1) > div > div.thumb_area > div')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



