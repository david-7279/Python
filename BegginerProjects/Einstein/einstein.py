# Global variable for the speed of light in meters per second
C = 300000000

def userInput():
    try:
      mass = input('Write the value of the mass: ')
      if mass.isdigit():
        return int(mass)
      else:
        print(f'Invalid number {mass}! Please, try again.')
        return None
    except ValueError:
      print('Invalid Value! Please, try again.')
      return None


def einsteinFormula(mass):
    if mass is not None:
      joules = mass * (C * C)
      return joules
    return None


def main():
  mass = None
  while mass is None:
    mass = userInput()
  formula = einsteinFormula(mass)
  print(f'\nE: {formula}')


if __name__ == "__main__":
    main()