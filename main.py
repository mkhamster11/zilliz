
from loadar import ModelManager
from vector_zilliz import deleteDataApi, getCount, insertDataApi,queryDataApi
import time
MODEL_GTE = ModelManager().get_model()


def insertData(item_list,collection_name="skills"):
    len_item_list = len(item_list)
    print("collection_name: ",collection_name)

    if len_item_list > 0: 
        
        for index,item in enumerate(item_list):
            print("**" * 30)
            print(f"Index: {index}/{len_item_list}")
            print(f"Skill: {item}")
            # Encode the skill using the model
            start_tiem =time.time()
            v1 = MODEL_GTE.encode(item)
            res=insertDataApi(item, v1.tolist(),collection_name=collection_name)
            end_tiem =time.time()
            print("TIME TAKEN",end_tiem-start_tiem)
            # # Decode the vector back to text
            print(f"Vector: {res}")
            print(f"DOne uploading Vector")
        return f"Done uploading all vectors {len_item_list} items"
    else:
        return "No items to upload"


def searchItem(item,collection_name="positions"):
    # Encode the skill using the model
    item_encode= MODEL_GTE.encode(item)
    res=queryDataApi(item_encode.tolist(),collection_name=collection_name,limit=15)
    item_list = res.get("data")
    # for match in item_list:
    #     print(f"Skill: {match.get('name')}")
    #     print(f"Distance: {match.get('distance')}")
    #     print("**" * 30)
    return item_list











# print(deleteDataApi(collection_name="skills",id_list=[458310408763908528]))
# print(searchItem("skill_name",collection_name='skills'))

# skill = "Python Java Go C# C++ PHP PySpark SQL MySQL Aurora MSSQL Oracle PostgreSQL"
# skill_list = [skill for skill in skill.split(" ") if skill.strip()]
# c= 0
# position = [
#     "Python Engineer",
#     "Senior Python Engineer",
#     "Backend Engineer – Python & Cloud",
#     "Data Engineer – Python & PySpark",
#     "Software Engineer – Cloud & Data Systems",
#     "Senior Backend Developer – AWS & Python",
#     "Big Data Engineer – Python & SQL"
# ]
# import time

# for position_item in position:
#     start_time = time.time()
#     print(f"Position: {position_item}")
#     _list=searchItem(position_item,collection_name='positions')
#     each_time = time.time()
#     print(f"Each req Time taken for {position_item}: {each_time - start_time}")
#     print(f"Response: {position_item}/{_list[0].get('name')}")
#     print(_list)
#     print("**" * 30)

# print(f"Total Time taken for {time.time() - start_time}")


# for index,item in enumerate(_list):
#     if item.get('name') in skill_list:
#         print(f"Skill: {item.get('name')}")
#         print(f"Distance: {item.get('distance')}")
#         print("**" * 30)
#         c+=1

#     print(f"Skill already exists in the list:{c}/{len(_list)}")
#     print(f"Index: {index+1}/{len(_list)}")

# print(skill_list)
# print(getCount('positions'))
# # Open and read a text file

# import csv

# with open('New Positions.csv', 'r', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     data = [row[0] for row in reader if row]

# insertData(data,collection_name="positions")