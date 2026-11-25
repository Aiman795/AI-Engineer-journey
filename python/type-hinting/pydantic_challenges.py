from pydantic import BaseModel,Field,EmailStr
# class Product(BaseModel):
#     name: str=Field(min_length=1)
#     price: float = Field(gt=0)
#     in_stock: bool = True
# #  1 validation error for product price Field required [type=missing, input_value={'name': 'aiman', 'age': 3.3, 'in_stock': 'yes'}, input_type=dict]
# p=Product(name="",price=-5,in_stock="ON")
# print(p)

class Contact(BaseModel):
    name:str=Field(min_length=1)
    email:EmailStr|None=None
    phone:str=Field(pattern=r"^\d{7,15}$")
# c=Contact(name="aiman",email="aiman.gmail.com",phone=123456) 2 validation errors for Contact email
# c=Contact(name="Aiman", phone="0300123456") passed
# c=Contact(name="", phone="abc") 2 validation errors for Contact name
# print(c)