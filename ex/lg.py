from collections import deque
q = int(input())
for i in range(q):
    n = int(input())
    pushed = deque(map(int,input().split()))
    poped = deque(map(int,input().split()))
    l = deque()
    for i in pushed:
        l.append(i)
        while l[-1] == poped[0]:
            poped.popleft()
            l.pop()
            if not l:
                break
    if l:
        print('No')
    else:
        print('Yes')