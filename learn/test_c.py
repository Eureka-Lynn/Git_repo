from io import StringIO

f=StringIO('哈比下\n奥利安frame\n哈里路大旋风')

while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())





from io import BytesIO

f=BytesIO()
f.write('阿弥诺斯'.encode('utf-8'))

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

print(f.read())