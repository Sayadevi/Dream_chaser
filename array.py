n=int(input())
s=input()
s1=s.split()
n=len(s1)
for i in range(0,n):
    l=int(s1[i])
    print(l,end=" ")
    print(i)
