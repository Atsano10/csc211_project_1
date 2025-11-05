a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','s','t','u','v','w','x','y','z']

c = input("Give me a word: ")

c1 = list(c)

for i in range (len(c)):
    if c1[i] in b:
        for j in range (len(b)):
            if b[j] == c1[i]:
                c1[i] = a[j]

c1 = "".join(c1)

print(c1)

##This was just done to get an idea of the actual code of a toUpper code.


