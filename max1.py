n=int(input())
n1=input()
n1=n1.split()
max=int(n1[0])
for i in range(1,n):
    c=int(n1[i])
    if(max<c):
        max=c
print(c) 
