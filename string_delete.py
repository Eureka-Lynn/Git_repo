a=input()
n=len(a)
x=0
L0=[]
L1=[]
for i in a[0:n]:
    L0.append(i)
while(x<n):
    if L0[x] not in L0[x+1:n]:
        L1.append(L0[x])
    else:
        pass
    x=x+1
print(L1)