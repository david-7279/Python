from consult import Consult
from time import sleep
import os, json

pet_categories = {
  "Cat": 0,
  "Dog": 0,
  "Fish": 0,
  "Turtle": 0,
  "Bird": 0,
  "Rabbit": 0,
  "Hamester": 0
}

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(0.5)

def inverse_clear_screen():
  sleep(0.9)
  os.system('cls' if os.name == 'nt' else 'clear')


class Pet():
  def __init__(self):
    self.pets = []
  

  def add_pet(self):
    while True:
      try:
        inverse_clear_screen()
        pet_name = input('Pet name: ').title()
        if not pet_name or pet_name.isdigit():
          print(f'Invalid pet name: {pet_name}. Please, write an valid name.\n')
          continue
        
        for index, category in enumerate(pet_categories, start=1):
          print(f'[{index}] {category}')
        pet_category = int(input('Pet category: '))
        if pet_category < 1 or pet_category > len(pet_categories) or not pet_category:
          print(f'Invalid pet category: {pet_category}. Please, choose an valid category.\n')
          continue
        
        pet_age = int(input('Pet age: '))
        if not pet_age or pet_age < 0:
          print(f'Invalid age: {pet_age}. Please, write an valid age.\n')
          continue
        
        category_name = list(pet_categories.keys())[pet_category - 1]
        self.pets.append({'name': pet_name, 'category': category_name, 'age': pet_age})
        print(f'Pet {pet_name} added sucessfully!\n')
        self.save_pet_list()
        inverse_clear_screen()
        return
      
      except ValueError:
        print(f'Invalid input. Please enter an number.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')
    

  def edit_pet(self):
    if not self.pets:
        print('No pets available.')
        return
    
    while True:
      try:
        self.view_pet()
        print('[0] Go back\n')
        pet_index = int(input('Choose a pet to edit: '))
        if 1 <= pet_index <= len(self.pets):
          edit_pet = self.pets[pet_index - 1]

          new_name = input(f'New name of the pet (Leave blank to keep the current "{edit_pet["name"]}"): ').title() or edit_pet['name']
                
          print('\nPet categories: ')
          for index, category in enumerate(pet_categories, start=1):
            print(f'[{index}] {category}')
                
          new_category_input = input(f'New category of the pet (Leave blank to keep the current "{edit_pet["category"]}"): ')
          new_category = list(pet_categories.keys())[int(new_category_input) - 1] if new_category_input else edit_pet['category']

          new_age_input = input(f'New age of the pet (Leave blank to keep the current "{edit_pet["age"]}"): ')
          if new_age_input:
            new_age = int(new_age_input) if new_age_input else edit_pet['age']
            if new_age <= 0:
              print(f'Invalid age: {new_age}. Please, try again.')
              inverse_clear_screen()
              continue
          else:
            new_age = edit_pet['age']

          edit_pet.update({
            "name": new_name,
            "category": new_category,
            "age": new_age
          })
                
          print(f'Pet updated successfully!\n')
          self.save_pet_list()
          inverse_clear_screen()
          return

        elif pet_index == 0:
          print('No changes made. All pets remain the same.\n')
          inverse_clear_screen()
          return
        else:
          print(f'Invalid pet: {pet_index}. Please, choose a valid pet.\n')
          inverse_clear_screen()

      except ValueError:
        print('Invalid input. Please, enter a number.\n')
        inverse_clear_screen()
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()


  def remove_pet(self):
    if not self.pets:
      print('No pets available.')
      return
    
    while True:
      try:
        self.view_pet()
        print('[0] Go back\n')

        pet_index = int(input('Choose an pet: '))
        if 1 <= pet_index <= len(self.pets):
          confirmation = input('Are you sure you want to remove the pet (Yes/No)? ').lower()
          if confirmation in ['yes', 'y']:
            remove_pet = self.pets.pop(pet_index - 1)
            print(f'Pet removed sucessfully: {remove_pet['name']}')
            self.save_pet_list()
            inverse_clear_screen()
            return
          else:
            print('No changes made. All pets remains the same.\n')
            inverse_clear_screen()
            return
        elif pet_index == 0:
          print('No changes made. All pets remains the same.\n')
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
    
    
  def view_pet(self):
    if not self.pets:
      print('No pets available.')
      return
    
    print('Your pets:')
    for index, pet in enumerate(self.pets, start=1):
      print(f'[{index}] {pet['name']} ({pet['category']}) is {pet['age']} years old.')
      

  def view_category_pet(self):
    if not self.pets:
      print('No pets available.')
      return
    
    while True:
      try:
        inverse_clear_screen()
        print('Your categoires:')
        for index, category in enumerate(pet_categories, start=1):
          print(f'[{index}] {category}')
        print('[0] Go back\n')

        category_index = int(input('Choose an category: '))
        if 1 <= category_index <= len(pet_categories):
          chosen_category = list(pet_categories.keys())[category_index - 1]
          print(f'Pets in category: [{chosen_category}]:')
          pets_in_category = [pet for pet in self.pets if pet['category'] == chosen_category]
          if pets_in_category:
            for pet in pets_in_category:
              print(f'- {pet['name']} (Age: {pet['age']})\n')
            return
          else:
            print(f'No pets found in {chosen_category}.\n')
            inverse_clear_screen()
            continue
          
        elif category_index == 0:
          print('No changes made. All pets remain the same.\n')
          inverse_clear_screen()
          return
        else:
          print(f'Invalid category: {category_index}. Please, write an valid category.\n')
          inverse_clear_screen()
          continue

      except ValueError:
        print('Invalid input. Please, enter a number.\n')
        inverse_clear_screen()
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()


  def view_consult(self):
    if not self.pets:
      print('No pets available.')
      return
    
    consult = Consult(self.pets)
    choices = [1, 2, 3, 4, 5, 6, 0]
    
    print('Here can manage your pets consult.\n')
    while True:
      try:
        print('1. for add consult')
        print('2. for edit consult')
        print('3. for remove consult')
        print('4. for view consult')
        print('5. for view consult by pet')
        print('6. mark completed consult')
        print('0. go back\n')

        option = int(input('Choose an option: '))
        if option in choices:
          if option == 1:
            clear_screen()
            consult.add_consult()
          elif option == 2:
            clear_screen()
            consult.edit_consult()
          elif option == 3:
            clear_screen()
            consult.remove_consult()
          elif option == 4:
            clear_screen()
            consult.view_consult()
          elif option == 5:
            clear_screen()
            consult.view_pet_consult()
          elif option == 6:
            clear_screen()
            consult.sucess_consult()
          elif option == 0:
            print('No changes made. All the consult remains the same.\n')
            inverse_clear_screen()
            return
        else:
          print(f'Invalid choice: {option}. Please, write an valid option.\n')
          inverse_clear_screen()
          continue

      except ValueError:
        print('Invalid input. Please, enter a number.\n')
        inverse_clear_screen()
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')
        inverse_clear_screen()

  
  def save_pet_list(self, filename='Pets.json'):
    if not self.pets:
      print('No pets available.')
      return

    try:
      pets_with_ids = []
      for index, pet in enumerate(self.pets, start=1):
        pet_with_id = {
          'ID': index,
          'name': pet['name'],
          'category': pet['category'],
          'age': pet['age']
        }
        pets_with_ids.append(pet_with_id)

      with open(filename, 'w') as file:
        json.dump(pets_with_ids, file, indent=4)
    except Exception as e:
      print(f'An error occurred while saving contacts: {e}\n')