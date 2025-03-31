from time import sleep
import os

class Utils:
  def __init__(self):
    pass
    
  def clear(self):
    os.system("cls" if os.name == "nt" else "clear")
    sleep(0.5)

  def clear_input(self):
    sleep(1)
    input('Press enter to continue...') 
    self.clear()