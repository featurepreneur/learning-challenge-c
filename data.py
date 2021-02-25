from pymongo import MongoClient
import  os
import pandas as pd
from flask import send_from_directory

client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
db = client['CrowdEngine']
doc = db['actress']
client.close()


movieslist = list(doc.find({'Actress Name': { '$exists': 'true' } },{'_id':0})) #list(doc.find({'movie': { '$exists': 'true' } },{'movie':1,'_id':0}))

#movieslist =  [i['Actress Name'] for i in movieslist]
#movieslist = list(set(movieslist))
size = len(movieslist)


def page(pg , index):

    actname =  [i['Actress Name'] for i in movieslist]
    if pg == 'next':
        if size-1 > index:
            return actname[index+1]
        elif size-1 == index:
            return actname[0]
    elif pg == 'pre':
        if index == 0 :
            return actname[size-1]
        else:
            return actname[index-1]

def write(**kwargs):
    client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
    db = client['CrowdEngine']
    doc = db['actress_data']     
    doc.insert_one({'Actress Name':kwargs['actor'],'Movie Count':kwargs['movie'],'Screen Duration':kwargs['duration'],'Instagram Followers':kwargs['insta'],'Dress match meter':kwargs['dress'],'Consistency':kwargs['consistency'],'Critic Score':kwargs['criticscore']})
    client.close()

def get_csv(a):
   
    client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
    db = client['CrowdEngine']
    doc = db['actress_data']  
    df = list(doc.find({}))
    df = pd.DataFrame(df)
    
    df = df.to_csv('pyhackons-actress-data.csv',index=False)
    path = os.path.abspath('pyhackons-actress-data.csv')
    print(path)
    client.close()
   
    #path = path[:-8] or path.replace('data.csv','')
    path = path.replace('pyhackons-actress-data.csv','')
    a.config["CLIENT_CSV"] = path
    return(send_from_directory(a.config["CLIENT_CSV"],filename='pyhackons-actress-data.csv',as_attachment=True) )
   
def table():
    client = MongoClient("mongodb+srv://pyhackons:pyhackons@cluster0.ajjz3.mongodb.net/crowdengine?retryWrites=true&w=majority")
    db = client['CrowdEngine']
    doc = db['actress_data']
    data1 = list(doc.find({},{'_id':0}) )
    client.close()
    return data1
