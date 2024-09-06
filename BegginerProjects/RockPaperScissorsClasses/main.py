from game import Game
from player import Player

def main():
  player = Player('David')
  player.make_choice('rock')

  game = Game(player)
  print(f'You chose: {player.choice} and computer chose: {game.cpu_choice}')
  print(game.winner())


if __name__ == '__main__':
  main()