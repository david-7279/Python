import random
from player import Player

class Game:
  options = ['rock', 'paper', 'scissors']

  def __init__(self, player):
    self.player = player
    self.cpu_choice = random.choice(Game.options)

  def winner(self):
      if self.player.choice == self.cpu_choice:
        return 'Draw!'
      elif (self.player.choice == 'rock' and self.cpu_choice == 'scissors') or (self.player.choice == 'paper' and self.cpu_choice == 'rock') or (self.player.choice == 'scissors' and self.cpu_choice == 'paper'):
        return f'{self.player.name} won!'
      else:
        return 'You lost!'