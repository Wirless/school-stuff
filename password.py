import hashlib

password = ""

def inputpass(password):
	password = input("Please enter a password: ")
	return password


def printpassword(password):
	passwords = inputpass()
	print(f"Your password is : {passwords}")
	

def hashpass(passworde):
	passworde = hashlib.sha256((passworde).encode('utf-8')).hexdigest()
	print(f"Your password is : {passworde}")
	return passworde