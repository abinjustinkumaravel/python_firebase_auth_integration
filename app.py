import firebase_admin
from firebase_admin import db
import json

cred_obj =firebase_admin.credentials.Certificate('path/to/serviceAccountKey.json')

default_app=firebase_admin.initialize_app(cred_obj,{
    'databaseURL': 'https://your-database-name.firebaseio.com'
})

ref =db.reference("/")

ref.set({
    "Books":
    {
        "Best_Sellers":-1
    }
})

ref = db.reference("/Books/Best_Sellers")


with open("data.json", "r") as f:
    file_contents =json.load(f)

ref.set(file_contents)

for key, value in file_contents.items():
    ref.push().set(value)






# ========================= Dta Modification ================================== 
# ref = db.reference("/Books/Best_Sellers")
# best_sellers =ref.get()
# print(best_sellers)

# for key, value in best_sellers.items():
#     if (value["Author"]=="J.R.R. Tolkien"):
#         ref.child(key).update({"Price":80})