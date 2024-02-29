class Student(object):
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age

s=Student()
s.age=23
print(s.age)
    