import datetime
birth_year = int(input("What year were you born? "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print("You are {age} years old now.")
input()
