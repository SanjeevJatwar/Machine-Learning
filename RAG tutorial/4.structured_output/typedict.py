from typing import TypedDict

class people(TypedDict):

    name :str
    age : int

new_person: people= {'name' : "sanju", 'age' :"12"}

print(new_person)