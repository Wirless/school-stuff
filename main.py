# logger
# 1. load user input
# 2. check for id in the list of file
# 3. add users or remove from the dict. storing dict in variable easiest?
# 4. for k,v in pairs[]
import password

### default dict user database
users = {
0:["FirstUser", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", "Patryk Zmyslony", True, 0],
1:["SecondUser", "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752", "John Wick", False, 0]
}
##globals and textprints
unsuccessfull = 3
welcomessage = "Hello Agent "
areyouadmin = "Administrator: "

###read/write options
f=open("logins.txt", "r")
#e=open("logins.txt", "w")
#content = e.write(str(users))

contente = f.read()
newdict = eval(contente)
#contente.users["0"][1]

#print(newdict["0"][1])

agentID = input("Please enter your agent ID:\n")


#

for k in newdict:
	if agentID == k in newdict:
		userNAME = input("Please enter your user name:\n")
		if userNAME == newdict[agentID][0]:
			pw = input("Please enter a password: ")
			pw = password.hashpass(pw)
			if pw == newdict[agentID][1]:
				print(welcomessage+newdict[agentID][2])
				print(areyouadmin+str(newdict[agentID][3]))
			else:
				print(f"{passworde}")
		else:
			print("wrong username")