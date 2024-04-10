class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 80 and self.score <= 100:
            return 'A'
        elif self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 0 and self.score < 60:
            return 'C'
        if self.score < 0 or self.score > 100:
            raise ValueError('invalid value:%s'% self.score)




s1 = Student('Bart', 80)
s2 = Student('Lisa', 100)
s3 = Student('Bart', 60)
s4 = Student('Lisa', 79)
s5 = Student('Bart', 0)
s6 = Student('Lisa', 59)
s7 = Student('Bart', -1)
s8 = Student('Lisa', 101)


print(s1.get_grade())
print(s8.get_grade())