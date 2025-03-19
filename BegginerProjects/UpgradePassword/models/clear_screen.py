from time import sleep
import os

def clear():
  os.system("cls" if os.name == "nt" else "clear")
  sleep(0.5)