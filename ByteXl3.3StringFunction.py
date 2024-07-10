import string
a =input()
b= input()
c =input()

a =''.join('*' if char.lower() in  'aeiou' else char for char in a)

b =''.join('@' if char.isalpha() and char.lower() not in 'aeiou' else char for char in b) )