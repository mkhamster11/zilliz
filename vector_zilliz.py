import http.client
import json
import requests


TOKEN ="1f9161428474f98ef959b59a4a56ed9d7c02dfc93d2f5f7339d65d09e0a207fac2c3b20210413f54a89e2f3915f49cbe8b266d65"


def insertDataApi(name,data,TOKEN=TOKEN,collection_name="sort_skills"):
    """
    Insert data into the Zilliz cloud database.
    """
    headers = {
            'Authorization': f"Bearer {TOKEN}",
            'Accept': "application/json",
            'Content-Type': "application/json"
        }
    url = "https://in03-97313d7f3a90d79.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/entities/insert"

    payload = json.dumps({"collectionName":collection_name,
               "data":[{"name":name,"vector":data}]})


    response = requests.post(url, data=payload, headers=headers)

    return response.json()


def queryDataApi(data,feilds:list=["name","distance"],collection_name="skills",limit=15):

    url = "https://in03-97313d7f3a90d79.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/entities/search"
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



def getDataApi(collection_name="skills",id_list=[]):
    url = "https://in03-97313d7f3a90d79.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/entities/get"
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
    url = "https://in03-97313d7f3a90d79.serverless.gcp-us-west1.cloud.zilliz.com/v2/vectordb/entities/delete"
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