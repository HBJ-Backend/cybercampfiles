username = input("Username: ")
password = input("Password: ")
if username == "john":
	if password == "Qwerty12#":
		print("Login Successfull")
	else:
		print("Wrong Password")
else:
	print("Wrong Username")