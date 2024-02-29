import sys
def test():
    args=sys.argv
    if len(args)==1:
        print('hello world')
    elif len(args)==2:
        print('hello %s'%args[0])
    else:
        print('fuck you')
    
if __name__=='__main__':
    print(test())