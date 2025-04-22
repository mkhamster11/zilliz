
from loadar import ModelManager
from vector_zilliz import insert_data,query_data
MODEL_GTE = ModelManager().get_model()



# # Open and read a text file
# with open('PromptsAshok.txt', 'r', encoding='utf-8') as file:
#     skill_list = file.read().strip().split(',')

# skill_list =skill_list[1:]

# for index,skill in enumerate(skill_list):
#     print("**" * 30)
#     print(f"Index: {index}")
#     print(f"Skill: {skill}")
#     # Encode the skill using the model
#     v1 = MODEL_GTE.encode(skill)
#     res=insert_data(skill, v1.tolist())
#     # # Decode the vector back to text
#     print(res.decode("utf-8"))
#     print(f"DOne uploading Vector")
#     print("**" * 30)



skill = "Py"
# Encode the skill using the model
v1 = MODEL_GTE.encode(skill)
res=query_data(v1.tolist())
for match in res.get("data"):
    if match.get("distance") >=0.8:
        print(f"Skill: {match.get('skill_name')}")
        print(f"Distance: {match.get('distance')}")
        print("**" * 30)