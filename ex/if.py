w=80.5
h=1.75
bmi=w/(h*h)
if bmi<18.5:
    print('too light')
elif bmi<=25 and bmi>=18.5:
    print(normal)
elif bmi>25 and bmi<=28:
    print('too heavy')
elif bmi>28 and bmi<=32:
    print('fat')
else:
    print('too fat')