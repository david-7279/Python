from time import sleep
import os

def clear():
  os.system("cls" if os.name == "nt" else "clear")
  sleep(0.5)

def clear_input():
  sleep(1)
  input('Press enter to continue...') 
  clear()