a = int(input())
b = list(map(int,input().split()))
ans = 0
cnm = []
for left in range(a-1):
    for right in range(left+1,a):
        cnm.append(b[left]+b[right])
for i in range(a):
    if b[i] in cnm:
        ans += 1
print(ans)