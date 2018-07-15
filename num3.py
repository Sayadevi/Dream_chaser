n=input()
n1=len(n)
c=0
for i in range(0,n1):
    if(ord(n[i])>=48 and ord(n[i])<=57):
        c=c+1
print(c) 
