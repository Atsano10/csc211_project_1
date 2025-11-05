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

##
# Basically checks if the input is uppercase(a) or in lowercase(b) 
# Then if the input is lowercase it finds what letter it is and copies the
# index and changes its value besed on the list of every ascii character
# After it just prints out the new uppercased word.
##

## 
# What kind of LOGIC can be implemented for project 1 CSC 211
# every letter has = [_,_,_,_,_,_,_,_] - 8 bits
# capital letter and lowercase letter differ from the the 5th bit. 
# If the letter is lowercase the 5th bit == 1, so inverting it would make it its capital letter.
# Anything else like a ?, or any non character does not have an uppercase so we can ignore it.
##



