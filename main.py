from src.class_insta import Insta
import json
with open('login.json') as json_data:
    data = json.load(json_data)
    for key in data:
       insta = Insta(data['password'],data['username'])

insta.instagram_action()
