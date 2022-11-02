from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@cluster0.rv3ttod.mongodb.net/test', tlsCAFile=ca)
db = client.hanghae_10_preliminary

travel_list = list(db.travel.find({},{'_id':False}))
data = db.travel.find_one({'city_kor':'루체른'})

print(data)