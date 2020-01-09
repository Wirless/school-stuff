import hashlib

password = ""

def inputpass(password = input("Please enter a password: ")):
	return password


def printpassword(password):
	passwords = inputpass()
	print(f"Your password is : {passwords}")
	

def hashpass(password):
	hash_thiss = hashlib.sha256((password).encode('utf-8')).hexdigest()
	print(f"Your password is : {hash_thiss}")
	
hashpass(password)