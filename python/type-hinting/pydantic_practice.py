from pydantic import BaseModel, ValidationError


# --- Part 1: a basic model ---
class User(BaseModel):
    name: str
    age: int


# u = User(name="Aiman", age=23)
# print(u)
# print(u.name, u.age)

# Try each of these ONE AT A TIME. Predict: success or ValidationError?
# u=User(name="Ali", age="25") success
# u= User(name="Ali", age="twenty")  ValidationError
# u=User(name="Ali")  ValidationError
# u=User(name="Ali", age=25.5)  ValidationError
# u=User(name=123, age=25)  ValidationError
# print(u)
# print(u.name, u.age)

# --- Part 2: catching the error ---
# try:
#     User(name="Ali", age="twenty")
# except ValidationError as e:
#     print(e)
#     print(e.errors())       # a list of dictionaries: read the keys
# 1 validation error for User
# age Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twenty', input_type=str]

# # --- Part 3: defaults and optional fields ---
# class Student(BaseModel):
#     name: str
#     age: int
#     email: str | None = None
#     gpa: float = 0.0
#     courses: list[str] = []

# # Try:
# s=Student(name="Sara", age=20) output :name='Sara' age=20 email=None gpa=0.0 courses=[] 
# s=Student(name="Sara", age=20, courses=["Math", "AI"]) output:name='Sara' age=20 email=None gpa=0.0 courses=['Math', 'AI']
# s=Student(name="Sara", age=20, courses="Math") output:1 validation error for Student courses
# s=Student(name="Sara", age=20, gpa="3.8") output: name='Sara' age=20 email=None gpa=3.8 courses=[]
# print(s)


# # --- Part 4: converting to and from dictionaries ---
# data = {"name": "Ali", "age": 22}
# user = User(**data)                  # same idea as Contact(**d)
# user2 = User.model_validate(data)    # the Pydantic way
# print(user.model_dump())             # like asdict() {'name': 'Ali', 'age': 22}
# print(user.model_dump_json())        # a JSON string {"name":"Ali","age":22}


# # --- Part 5: nested models ---
class Address(BaseModel):
    city: str
    country: str


class Employee(BaseModel):
    name: str
    address: Address
    skills: list[str]


emp = Employee(
    name="Hamza",
    # address={"city": "Islamabad", "country": "Pakistan"},   # a dict becomes an Address
    skills=["Python", "FastAPI"],
)
print(emp.address.city) 
# output: Islamabad
