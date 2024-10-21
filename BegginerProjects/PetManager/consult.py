from time import sleep
import os

# Clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(0.5)

def inverse_clear_screen():
    sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')


class Consult():
  def __init__(self, pets):
    self.consults = []
    self.pets = pets

  def view_pets(self):
    print('Your pets:\n')
    for index, pet in enumerate(self.pets, start=1):
      print(f'[{index}] {pet["name"]} ({pet["category"]}) is {pet["age"]} years old')
    print('[0] to go back\n')

  def add_consult(self):
    while True:
      try:
        self.view_pets()
        
        pet_index = int(input('Choose a pet for the consult: '))
        if 1 <= pet_index <= len(self.pets):
          choosen_pet = self.pets[pet_index - 1]
          consult_date = input(f'Schedule a consult for {choosen_pet["name"]} (Date): ')
          self.consults.append({
            "name": choosen_pet["name"],
            "category": choosen_pet["category"],
            "age": choosen_pet["age"],
            "date": consult_date,
          })
          print(f'Consult for {choosen_pet["name"]} scheduled on {consult_date}\n')
          return

        elif pet_index == 0:
          print('No changes made. All the consults remain the same.\n')
          inverse_clear_screen()
          return
        else:
          print(f'Invalid pet: {pet_index}. Please, choose a valid pet.\n')
          inverse_clear_screen()
          continue

      except ValueError:
        print('Invalid input. Please, enter a number.\n')
        inverse_clear_screen()
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()


  def edit_consult(self):
    pass


  def remove_consult(self):
    pass


  def view_consult(self):
    if not self.pets:
      print('No pets available for consults.')
      return
    print('Scheduled consults:')
    for consult in self.consults:
      print(f'- {consult['name']}: {consult['date']}\n')


  def view_pet_consult(self):
    pass


  def sucess_consult(self):
    pass
