from pydantic import validate_call,BaseModel
@validate_call
def create_user(name:str,age:int)-> dict[str, str | int]: #dict key,value
    return {
        "Name":name,
        "Age":age,
    }
user1=create_user("aiman",23)
#user1=create_user("aiman","twenty") error
#user1=create_user("aiman","23") validate_call converts "23" into 23 so correct
print(user1)




class User(BaseModel):
    name: str
    age: int

user = User(name="aiman")   # raises ValidationError