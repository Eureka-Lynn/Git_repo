def check(n):
    import re
    if re.match(r'^([a-z]+)\.?([a-z]+)@([a-z]+).com$',n):
        return True
    else:
        return False


if __name__=='__main__':
    print(check('dada@jsdla.com'))