# ------------------------------------------------------------------
# Name:        main.py
# Purpose:     Main module running the whole software
# Author:      PZmyslony
# Created:     9/01/2020
# Revision:    1.00
# --------------------------------------------------------------------

# -- IMPORTS --
import login
import reusables
# -- GLOBALS/CONSTANTS --
welcomessage = "Hello Agent "
areyouadmin = "Administrator: "

# -- FUNCTIONS/CLASSES --

def mainmenu():
	if success[0] == True:
		reusables.clearscreen()
		print("IM IN")
		print(welcomessage+success[1])
		print(areyouadmin+success[2])
	else:
		print("I failed the login")

agentID = login.getinput()
success = login.loggingin(agentID)	
mainmenu()