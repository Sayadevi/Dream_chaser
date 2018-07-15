n=input()
n1=n.split()
a=int(n1[0])
b=int(n1[1])
l1=[]
for i in range(a,b):
    f=i
    a1=0
    while(f!=0):
        r=f%10
        a1=a1+(r**3)
        t=f//10
        f=t
    if(a1==i):
        l1.append(i)
for i in l1:
    print(i,end=" ")
