import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s:'%(text,func.__name__))
            return func(*args,*kw)
        return wrapper
    return decorator



@log('阿弥诺斯')

def now():
    print('a')

print(now())
print(now.__name__)