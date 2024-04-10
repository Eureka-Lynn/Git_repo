from collections import deque
import time

start1=time.time()
q=deque(['a','b','c'])
for i in range(1000000):
    q.append('x')
end1=time.time()
print('deque',end1-start1)

start2=time.time()
L=['a','b','c']
for i in range(1000000):
    L.append('d')
end2=time.time()
print('list',end2-start2)