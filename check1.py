n=input()
vowels=["a","e","i","o","u"]
c=ord(n)
if c>=97 and c<=122:
    if n in vowels:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
