for i in range(1000,10000):
 r=i**0.5
 if int(r)*int(r)==i:
   if all(int(d)%2==0 for d in str(i)):
    print(i)
    
