startYear=int(input("Enter the start year:"))
print("Enter the last year")
endYear=int(input("Enter the end year:"))
print("List of leap years:")
#loop through between the start and end year
for year in range(startYear,endYear):
#check if the year is a leap year
  if((year%4==0)and(year%100!=0))or(year%400==0):
   print(year)
