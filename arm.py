n=int(input("Enter number:"))
a=n%10
b=(n//10)%10
c=n//100
s=a**3+b**3+c**3
print("Armstrong" if s==n else"Not")
