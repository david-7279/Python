import json
from time import sleep
import os

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(1)


class Contact():
  def __init__(self):
    self.contact_list = []

  
  def add_contact(self):
    while True:
      try: 
        os.system('cls' if os.name == 'nt' else 'clear')

        name = input('Name: ').title()
        if not name:
          print(f'Invalid name: {name}. Please, write an valid name.\n')
          sleep(1)
          continue
        phone = input('Phone number: ')
        if not phone or len(phone) < 8:
          print(f'Invalid phone number: {phone}. Please, write an valid phone number (min 8 digits).\n')
          sleep(1.3)
          continue
        email = input('Email: ')
        if not email or '@' not in email:
          print(f'Invalid email: {email}. Please, write an valid email.\n')
          sleep(1.3)
          continue

        contact = {
          "name": name,
          "phone": phone,
          "email": email
        }

        self.contact_list.append(contact)
        print(f'Contact added sucessfully into the list.')
        self.save_contact_list()
        sleep(0.7)
        clear_screen()
        return
        
      except ValueError:
        print('Invalid contact. Please, try again.')
      except TypeError:
        print('Invalid contact. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
    
  def view_contact_list(self):
    if not self.contact_list:
      print('No contact in the list available.\n')
      return
    
    print('Your contacts: ')
    for index, contact in enumerate(self.contact_list, start=1):
      print(f'[{index}] {contact['name']}, Phone Number: {contact['phone']} - {contact['email']}')
    print('')

  
  def edit_contact(self):
    if not self.contact_list:
      print('No contact in the list available.\n')
      return
    
    self.view_contact_list()
    print('[0] To leave\n')

    while True:
      try:
        contact_index = int(input('Choose an index to change the contact: '))  
        if 1 <= contact_index <= len(self.contact_list):
          updated_contact = self.contact_list[contact_index - 1]

          new_name = input(f'New contact name: (Leave blank to keep current "{updated_contact['name']}"): ').title() or updated_contact['name']

          new_phone_input = input(f'New contact phone: (Leave blank to keep current "{updated_contact['phone']}"): ')
          new_phone = int(new_phone_input) if new_phone_input else updated_contact['phone']

          new_email = input(f'New contact email: (Leave blank to keep current "{updated_contact['email']}"): ') or updated_contact['email']

          updated_contact.update({
            "name": new_name,
            "phone": new_phone,
            "email": new_email
          })

          print(f'Contact updated: {updated_contact['name']}, Phone Number: {updated_contact['phone']} - {updated_contact['email']}\n')
          self.save_contact_list()
          return
        elif contact_index == 0:
          print('No changes made. All the contact list remains the same.\n')
          return
        else:
          print(f'No contact with the index {contact_index} found. Please, try again.')

      except ValueError:
        print(f'Invalid number: {contact_index}. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')


  def remove_contact(self):
    if not self.contact_list:
      print('No contact in the list available.\n')
      return

    self.view_contact_list()
    print('[0] To leave\n')

    while True:
      try:
        contact_index = int(input('Choose an index to remove the contact: '))
        if 1 <= contact_index <= len(self.contact_list):
          confirmation = input('Are your sure you want to remove the contact (Yes/No)? ').lower()
          if confirmation == 'yes' or confirmation == 'y':
            removed_contact = self.contact_list.pop(contact_index - 1)
            print(f'Contact removed sucessfully: {removed_contact['name']}, Phone Number: {removed_contact['phone']} - {removed_contact['email']}\n')
            self.save_contact_list()
            return
          else:
            print('No changes made. All the contact list remains the same.\n')
            return
        elif contact_index == 0:
          print('No changes made. All the contact list remains the same.\n')
          return

      except ValueError:
        print(f'Invalid number: {contact_index}. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
    

  def save_contact_list(self, filename='Contact.json'):
    if not self.contact_list:
      print('No contact in the list available.\n')
      return

    try:
      with open(filename, 'w') as file:
        json.dump(self.contact_list, file, indent=4)
    except Exception as e:
      print(f'An error occurred while saving contacts: {e}\n')
  

  def load_contact_list_file(self, filename='Contact.json'):
    try:
      with open(filename, 'r') as file:
        self.contact_list = json.load(file)
        print('Contacts loaded successfully!\n')
    except FileNotFoundError:
      print(f'File {filename} not found. No contacts loaded.\n')
    except json.JSONDecodeError:
      print(f'Error decoding {filename}. The file may be corrupted.\n')
    except Exception as e:
      print(f'An error occurred while loading contacts: {e}\n')