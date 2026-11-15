import json

test_data = """
{
    "company": "TechNova",
    "founded": 2019,
    "active": true,
    "address": 
    {
        "city": "Islamabad",
        "country": "Pakistan"
    },
    "employees": 
    [
        {"name": "Hamza", "role": "Backend Developer", "skills": ["Python", "FastAPI", "PostgreSQL"], "manager": null},
        {"name": "Zainab", "role": "ML Engineer", "skills": ["Python", "PyTorch"], "manager": "Hamza"}
    ]
}
"""

data = json.loads(test_data)

print(data)

print(data["address"]["city"])

for person in data['employees']:
    print(person['name'])

for person in data['employees']:
    del person['manager']
new_string=json.dumps(data,indent=2)
print(new_string)


# try:
#     data = json.loads(test_data)
# except json.JSONDecodeError as e:
#     print("Invalid JSON:", e)