# ------------------------------------------------------------------
# Name:        reusables.py
# Purpose:     reusables for various code that dont fit elsewhere
# Author:      PZmyslony
# Created:     9/01/2020
# Revision:    1.00
# ------------------------------------------------------------------

# -- IMPORTS --
import os
# -- GLOBALS/CONSTANTS --


# -- FUNCTIONS/CLASSES --



def clearscreen():
  '''
  clear screen of the console
  '''
  os.system('cls')
  os.system('clear')

def titleprint(agentname,admininfo):
  '''
  print the title and Agent name + administrator privileges
  '''
  print("*"*50)
  print("Agent: "+agentname)
  print(" ")
  print(" "*20+"UltraDecrypt0r")
  print(" ")
  print("\t\t\t\t\t\t\tAdministrator: "+admininfo)
  print("*"*50)

