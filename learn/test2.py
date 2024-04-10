class Myobject(object):
    def __init__(self):
        self.x=9

    def power(self):
        return self.x*self.x
    
obj=Myobject()

fn=getattr(obj,'power')
print(fn)
print(fn())
print(obj.power())