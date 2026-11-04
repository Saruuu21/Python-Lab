import os
import math
import datetime
import random

now = datetime.datetime.now()
print("Date:", now.date())
print("Time:", now.time())

current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

print(math.sqrt(25))  

print(random.randint(1, 10))
print(random.choice(["Python", "Java", "C++", "JavaScript"]))
