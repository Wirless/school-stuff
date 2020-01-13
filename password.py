# ------------------------------------------------------------------
# Name:        password.py
# Purpose:     password module for encrypting passwords with sha256
# Author:      PZmyslony
# Created:     9/01/2020
# Revision:    1.00
# ------------------------------------------------------------------

# -- IMPORTS --
import hashlib

# -- GLOBALS/CONSTANTS --
password = ""

# -- FUNCTIONS/CLASSES --


def inputpass(password):
	'''
	take input of password
	return the said password
	(str) -> str
	>>>password
	
	>>>test123
	
	
	'''
	password = input("Please enter a password: ")
	return password


def printpassword(password):
	'''
	take inputed password and print it to screen
	(str) -> str
	
	>>>password
	password
	>>>test123
	test123
	'''
	passwords = inputpass()
	print(f"Your password is : {passwords}")
	

def hashpass(passworde):
	'''
	Encrypt a password from input
	(str) -> str
	>>>test
	9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
	>>>password
	5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
	'''
	passworde = hashlib.sha256((passworde).encode('utf-8')).hexdigest()
	#print(f"Your password is : {passworde}")
	return passworde