import json

class Student(object):
    def __init__(self,name,age,score) -> None:
        self.name=name
        self.age=age
        self.score=score


s=Student('bob',20,245)
print(json.dumps(s,default=lambda obj:obj.__dict__))