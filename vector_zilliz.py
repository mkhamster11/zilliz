import http.client
import json
import requests


TOKEN =""
# URL = "https://in03-97313d7f3a90d79.serverless.gcp-us-west1.cloud.zilliz.com"
URL = "https://in01-296b8468e8e86ef.gcp-us-west1.vectordb.zillizcloud.com:443" ## paid
def insertDataApi(name,data,TOKEN=TOKEN,collection_name="sort_skills"):
    """
    Insert data into the Zilliz cloud database.
    """
    headers = {
            'Authorization': f"Bearer {TOKEN}",
            'Accept': "application/json",
            'Content-Type': "application/json"
        }
    url = f"{URL}/v2/vectordb/entities/insert"

    payload = json.dumps({"collectionName":collection_name,
               "data":[{"name":name,"vector":data}]})


    response = requests.post(url, data=payload, headers=headers)

    return response.json()


def queryDataApi(data,feilds:list=["name","distance"],collection_name="skills",limit=15):

    url = f"{URL}/v2/vectordb/entities/search"
    payload = json.dumps({
                "collectionName":collection_name,
                "data":[data],
                "limit": limit,
                "outputFields": feilds})
    headers = {
    "Authorization": F"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()

def getCount(collection_name):
    url = f"{URL}/v2/vectordb/collections/get_stats"
    headers = {
    "Authorization": F"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    payload = json.dumps({
        "collectionName":collection_name
    })
    response = requests.post(url,data=payload,headers=headers)
    try:
        return response.json()['data']
    except Exception as e:
        return e

def getDataApi(collection_name="skills",id_list=[]):
    url = f"{URL}/v2/vectordb/entities/get"
    payload = json.dumps({
                "collectionName":collection_name,
                "filter": f"Auto_id in {id_list}"})
    headers = {
    "Authorization": F"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()

def deleteDataApi(collection_name="skills",id_list=[]):
    url = f"{URL}/v2/vectordb/entities/delete"
    payload = json.dumps({
                "collectionName":collection_name,
                "filter": f"Auto_id in {id_list}"})
    headers = {
    "Authorization": F"Bearer {TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()