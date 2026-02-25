username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "1234":
        print("Login Successfull")
    else:
        print("Password is incorrect try again")

else:
    print("Wrong username")