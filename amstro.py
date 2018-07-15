n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
l1=[]
for i in range(a,b+1):
    f=i
    a1=0
    while(f!=0):
        r=f%10
        a1=a1+(r**3)
        t=f//10
        f=t
    if(a1==i):
        l1.append(a1)
for i in l1:
    print(i,end=" ")
