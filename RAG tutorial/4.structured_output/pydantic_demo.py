from pydantic import BaseModel

class people(BaseModel):

    name :str
    age : int

#new_person : people = {'name' : "sanju", 'age' :"12"}
# above one can also be written as :
new_person= {'name' : "sanju", 'age' :"12"}
Person = people(**new_person) 
print(new_person)