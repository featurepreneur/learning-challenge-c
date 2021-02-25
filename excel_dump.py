from flask import Flask
import data
import xlrd
from flask_pymongo import PyMongo
from decouple import config
from datetime import datetime

app = Flask(__name__ )

app.config["MONGO_URI"]=config("MONGO_URI")
mongo=PyMongo(app)
Learning=mongo.db.Learning_Challenge_Entries

loc = ("crowdchallenge.xlsx")

book = xlrd.open_workbook("crowdchallenge.xlsx")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
 
sheet.cell_value(0, 0)

row_val=sheet.row_values(1)

# datetime object containing current date and time
now = datetime.now()
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	

data={
    'name':row_val[0],
    'Entrylink':row_val[1],
    'Content':row_val[2],
    'Added_at':dt_string
}

Learning.insert_one(data)

print(data)