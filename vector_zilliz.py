import http.client
import json


TOKEN =""
conn = http.client.HTTPSConnection("in03-97313d7f3a90d79.serverless.gcp-us-west1.cloud.zilliz.com")
headers = {
        'Authorization': f"Bearer {TOKEN}",
        'Accept': "application/json",
        'Content-Type': "application/json"
    }

def insert_data(skill_name,data,headers=headers,conn=conn,collection_name="sort_skills"):
    """
    Insert data into the Zilliz cloud database.
    """


    payload = json.dumps({"collectionName":collection_name,
               "data":[{"skill_name":skill_name,"vector":data}]})


    conn.request("POST", "/v2/vectordb/entities/insert", payload, headers)

    res = conn.getresponse()

    return res.read()


def query_data(data,headers=headers,conn=conn,collection_name="sort_skills",limit=10):
    """
    Query data from the Zilliz cloud database.
    """

    payload = json.dumps({
               "collectionName":collection_name,
               "data":[data],
                "limit": limit,
                "outputFields": [
                    "*"
                ]})


    conn.request("POST", "/v2/vectordb/entities/search", payload, headers)

    res = conn.getresponse()

    return json.loads(res.read())
