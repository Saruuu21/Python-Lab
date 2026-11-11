class bank:
  def __init__(self,acc_no,name,acc_type,balance):
    self.acc_no=acc_no
    self.name=name
    self.acc_type=acc_type
    self.balance=balance
  def deposit(self,amount):
    self.balance=self.balance+amount
    print("Amount deposisted successfully")
  def withdraw(self,amount):
    if amount<=self.balance:
       self.balance=self.balance-amount
       print("Amount withdrawn successfully")
    else:
       print("Insufficient Balance")
       
  def display(self):
    print("Account Number:",self.acc_no)
    print("Name:",self.name)
    print("Account Type:",self.acc_type)
    print("Balance:",self.balance)
b1=bank(101,"Varsha","Savings",5000)
b1.display()
n1=int(input("Enter the amt to deposit:"))
b1.deposit(n1)
print("Balance after deposit:",b1.balance)
n2=int(input("Enter the amt that have to be withdraw:"))
b1.withdraw(n2)
print("Balance after withdrawal:",b1.balance)
  
