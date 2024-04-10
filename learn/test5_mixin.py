class Animal(object):
    pass
class Mammal(object):
    pass
class Bird(object):
    pass
class Dog(object):
    pass
class Bat(object):
    pass
class Parrot(object):
    pass
class OStrich(object):
    pass
class Runable(object):
    def run(self):
        print('running')
class Flyable(object):
    def flt(self):
        print('flying')
class Dog(Mammal,Runable):
    pass
class Bat(Mammal,Flyable):
    pass
