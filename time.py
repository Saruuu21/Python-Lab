class time:
  def __init__(self,h,m,s):
    self._hour=h
    self._minute=m
    self._second=s
  def __add__(self,t):
    h=self._hour+t._hour
    m=self._minute+t._minute
    s=self._second+t._second
    
    if s>=60:
      m= m+s//60
      s= s%60
    if m>=60:
      h= h+m//60
      m= m%60
    return time(h,m,s)
  def display(self):
    print("Time:",self._hour,":",self._minute,":",self._second)
t1=time(2,45,50)
t2=time(1,30,20)
t3=t1+t2
t3.display()
