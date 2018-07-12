n=input()
l=len(n)
c=0
for i in range(0,l):
    d=ord(n[i])
    if d>=97 and d<=122:
        c=c+1
if(c==l):
    print("Alphabet")
else:
    print("No")
