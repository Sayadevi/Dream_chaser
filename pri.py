n=input()
n=n.split()
a=int(n[0])
b=int(n[1])
l1=[]
for j in range(a+1,b):
    for i in range(2,j):
        if(j%i==0):
            flag=1
            break
    else:
        flag=0
    if(flag==0):
        l1.append(j)
for i in l1:
    print(i,end=" ")
