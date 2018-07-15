n=int(input())
n1=1
n2=0
for i in range(0,n):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
