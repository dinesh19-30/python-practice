username=input("Enter you name: ")

if len(username) > 12:
    print("your username can't be more than 12 characters")
elif not username.find(" ")==-1:
    print("your username can't be contain spaces")
elif not username.isalpha():
    print("your username can't contain numbers")
else:
    print(f"welcome {username}")           