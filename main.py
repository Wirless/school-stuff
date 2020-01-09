# logger
# 1. load user input
# 2. check for id in the list of file
# 3. add users or remove from the dict. storing dict in variable easiest?
# 4. for k,v in pairs[]



users = {
0:["FirstUser", "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", "Patryk Zmyslony", True, 0],
1:["SecondUser", "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752", "John Wick", False, 0]
}
unsuccessfull = 3
#if users["0"][1] == password:
welcomessage = "Hello Agent "

f=open("logins.txt", "r")
#e=open("logins.txt", "w")
#content = e.write(str(users))

contente = f.read()
newdict = eval(contente)
#contente.users["0"][1]

#print(newdict["0"][1])

agentID = input("Please enter your agent ID:\n")

for k in newdict:
	if agentID == k in newdict:
		print(welcomessage+newdict[agentID][2])
