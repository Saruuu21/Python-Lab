n=int(input("Enter your age"))
vote=lambda n:"Eligible to vote"if n>=18 else("Not Eligible to vote")
print(vote(n))

