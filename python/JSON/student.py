import json
# with open ('student.json','r') as s:
#     data=json.load(s)
# print(data)
try:
    data = json.loads(test_data)
except json.JSONDecodeError as e:
    print("Invalid JSON:", e)