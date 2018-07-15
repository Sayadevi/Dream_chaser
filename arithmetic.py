n1=input()
n2=n1.split()
n=int(n2[0])
a=int(n2[1])
d=int(n2[2])
f=0
for i in range(0,n):
    f=f+(a+(i*d))
print(f)
