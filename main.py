
from loadar import ModelManager
from vector_zilliz import insertDataApi,queryDataApi
import time
MODEL_GTE = ModelManager().get_model()





def insertData(item_list_str,collection_name="skills"):
    item_list = item_list_str.split(",")
    len_item_list = len(item_list)
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



def searchItem(item,collection_name="skills"):
    # Encode the skill using the model
    item_encode= MODEL_GTE.encode(item)
    res=queryDataApi(item_encode.tolist(),collection_name=collection_name,limit=15)
    item_list = res.get("data")
    # for match in item_list:
    #     print(f"Skill: {match.get('name')}")
    #     print(f"Distance: {match.get('distance')}")
    #     print("**" * 30)
    return item_list



skill = "python programming" 
_list=searchItem(skill)
print(_list)



# # Open and read a text file
# with open('PromptsAshok.txt', 'r', encoding='utf-8') as file:
#     skill_list = file.read().strip().split(',')
#     insertData(skill_list[2745:],collection_name="skills")