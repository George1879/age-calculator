import datetime
while True:
    birth_year = int(input("What year were you born? "))
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    print(f"You are {age} years old now.")
    choice = input("Do you want to go again? (yes or no) ")
    if choice == 'yes':
        print("enjoy")
    elif choice == 'no':
        print ("Ok, quitting now")
        break
    else:
        print("i'll assume that means yes")
