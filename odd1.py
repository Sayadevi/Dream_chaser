n=input()
n1=n.split()
c=int(n1[0])
m=int(n1[1])
for i in range(c+1,m):
    if(i%2!=0):
        print(i,end=" ")
