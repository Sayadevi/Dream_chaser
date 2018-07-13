n=input()
n1=n.split()
l=len(n1)
max=int(n1[0])
for i in range(1,l):
    c=int(n1[i])
    if(max<c):
        max=c
print(max)
