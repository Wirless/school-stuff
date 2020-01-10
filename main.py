import login




def mainmenu():
	if success == True:
		print("IM IN")
	else:
		print("I failed the login")

agentID = login.getinput()
success = login.loggingin(agentID)	
mainmenu()