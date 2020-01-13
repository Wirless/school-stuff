# ------------------------------------------------------------------
# Name:        login.py
# Purpose:     Login module for authorizing users
# Author:      Pzmyslony
# Created:     9/1/2020
# Revision:    1.00
# ------------------------------------------------------------------

# -- IMPORTS --
import password

# -- GLOBALS/CONSTANTS --
unsuccessfull = 3


# -- FUNCTIONS/CLASSES --




# logger
# 1. load user input
# 2. check for id in the list of file
# 3. add users or remove from the dict. storing dict in variable easiest?

# default dict user database to update to file
users = {
0:["FirstUser", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", "Patryk Zmyslony", True, 0],
1:["SecondUser", "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752", "John Wick", False, 0]
}

#read/write options
#comment the ones that are unused
#read for reading from file
f=open("logins.txt", "r")
#write uncomment when writing or editing main dict users
#e=open("logins.txt", "w")
#uncomment when you want to update the file
#content = e.write(str(users))

#read the content of the logins.txt
contente = f.read()
#eval to parse expression of dict from string from logins.txt
newdict = eval(contente)

#example of reading the users from dict
#contente.users["0"][1]

#print(newdict["0"][1])
def getinput():
	'''
	(num) -> num
	inputs agentID returns it to the next 
	function or returns error when input is not a integer.
	>>>1
	Please enter your user name:
	>>>blabla
	Not a number!
	'''
	get = True
	while get:
		try:
			agentID = int(input("Please enter your agent ID:\n"))
			return agentID
		except ValueError:
			print("Not a number!")

#

def loggingin(agentID):
	'''
	(agentID, userNAME,pw) -> bool
	takes agentID from getinput and checks if it exists within the database of users from the dict that was parsed via eval() previously then takes userNAME and checks whether it is correct later allowing to type in password that gets hashed from password.py function called hashpass() and compares the two sha256 strings if they are the same it grants user with information such as welcome message and his name and whether he has Administrator Privileges.
	>>>FirstUser
	Please enter a password:
	>>>test
	Hello Agent Patryk Zmyslony
	Administrator: True
	'''
	if agentID in newdict:
		global unsuccessfull
		while unsuccessfull >= 1:
			userNAME = input("Please enter your user name:\n")
			if userNAME == newdict[agentID][0]:
				while unsuccessfull >= 1:
					pw = input("Please enter a password: ")
					pw = password.hashpass(pw)
					if pw == newdict[agentID][1]:
						return True,newdict[agentID][2],str(newdict[agentID][3])
					else:
						print(f"error wrong password")
						unsuccessfull -= 1
				else:
					print("You typed the password wrong 3 times")
			else:
				print("wrong username")
				unsuccessfull -= 1
		else:
			print("Failed to input user name 3 times")

#sample of full print of all information per user was used to navigate through for loggingin() while it was written
#				print(newdict[agentID][0]+newdict[agentID][1]+newdict[agentID][2]+str(newdict[agentID][3])+str(newdict[agentID][4]))
