from time import sleep
import os

def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")
  sleep(0.5)