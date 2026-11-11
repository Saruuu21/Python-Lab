class rectangle:
 def __init__(self,length,breadth):
   self.length=length
   self.breadth=breadth
 def area(self):
   return self.length*self.breadth
 def perimeter(self):
   return 2*(self.length+self.breadth)
   
r1=rectangle(10,6)
r2=rectangle(7,4)

print("Rectangle 1")
print("Area:",r1.area())
print("Perimeter:",r1.perimeter())
print("Rectangle 2")
print("Area:",r2.area())
print("Perimeter:",r2.perimeter())

if r1.area()>r2.area():
  print("\n Rectangle 1 has greater area")
elif r1.area()<r2.area():
  print("\n Rectangle 2 has greater area")
else:
  print("\n Both rectangle have equal area")
