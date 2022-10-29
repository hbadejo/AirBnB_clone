from uuid import uuid4
from datetime import datetime
from models.base_model import BaseModel
from models import storage

# tformat = "%Y-%m-%dT % H: % M: % S. % f"
# time_now = datetime.now()

# print(time_now)

# print(datetime.today())
# print()
# x = uuid4()
# y = uuid4()
# z = uuid4()

# print(f'X val is {str(x)}, Y val is {str(y)}, Z val is {z}')

# ------3. BaseModel Test
# my_model = BaseModel()
# my_model.name = "My First Model"
# my_model.my_number = 89
# print(my_model)
# my_model.save()
# print(my_model)
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
#           type(my_model_json[key]), my_model_json[key]))


# ------4. Create BaseModel from dictionary
# my_model = BaseModel()
# my_model.name = "My_First_Model"
# my_model.my_number = 89
# print(my_model.id)
# print(my_model)
# print(type(my_model.created_at))
# print("--")
# my_model_json = my_model.to_dict()
# print(my_model_json)
# print("JSON of my_model:")
# for key in my_model_json.keys():
#     print("\t{}: ({}) - {}".format(key,
#           type(my_model_json[key]), my_model_json[key]))

# print("--")
# my_new_model = BaseModel(**my_model_json)
# print(my_new_model.id)
# print(my_new_model)
# print(type(my_new_model.created_at))

# print("--")
# print(my_model is my_new_model)

# ---------- 5. Store first Object

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
