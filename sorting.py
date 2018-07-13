n1=int(input())
n2=input()
n3=n2.split()
c=sorted(n3)
l=len(c)
for i in range(0,l):
    print(c[i],end=" ")
