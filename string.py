s=input("enter a string:")
print(s)
char=s[0]
s=s.replace(char,'$')
s=char+s[1:]
print(s)
