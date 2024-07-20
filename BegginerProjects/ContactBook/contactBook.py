from time import sleep
import os

contactList = []

def clearScreen():
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')


def userOption():
    choices = [1, 2, 3, 4, 5, 6]
    while True:
      try:
        option = int(input('Choose an option: '))
        if option in choices:
          return option
        else:
          print(f'Invalid option {option}! Please, try again.\n')

      except ValueError as error:
        print(f'Error: Invalid value {error}! Please, try again.\n')


def addContact():
    phoneNumber = input('Enter the phone number (9 digits): ').strip()
    name = input('Enter the name: ').strip()
    email = input('Enter the email address: ').strip()

    if len(phoneNumber) == 9 and name:
      contactList.append({'phoneNumber': phoneNumber, 'name': name, 'email': email})
      print(f'Contact {name} added sucessfully.')
      return True
    else:
      print(f'\nInvalid phone number "{phoneNumber}"! The phone number needs 9 digits and the name cannot be empty. Please, try again.')
      return False


def viewContactList():
    if not contactList:
      print('Contact list is empty!\n')
      return

    for contact in contactList:
      print(f'Name: {contact['name']}, Phone Number: {contact['phoneNumber']}, Email: {contact['email']}')


def deleteContact():
    if not contactList:
      print('Contact list is empty!\n')
      return
   
    viewContactList()

    try:
      phoneNumberToDelete = input('Enter the phone number to delete: ').strip()
      for contact in contactList:
        if phoneNumberToDelete == contact['phoneNumber']:
          contactList.remove(phoneNumberToDelete)
          print(f'Contact with phone number "{phoneNumberToDelete}" removed sucessufully!\n')
        else:
          print(f'Invalid phone number {phoneNumberToDelete}! Please, try again.\n')
    except ValueError as error:
      print(f'Error: Invalid value {error}! Please, try again.\n')


def updateContact():
    if not contactList:
      print('Contact list is empty!\n')
      return
   
    viewContactList()

    try:
      phoneNumberToUpdate = input('Enter the phone number to update: ').strip()

      for contact in contactList:
        if phoneNumberToUpdate == contact['phoneNumber']:
          print(f'Updating: [{contact['phoneNumber']}] {contact['name']} - {contact['email']}')

          newPhoneNumber = input(f'New phone number (leave blank to keep current): ').strip() or contact['phoneNumber']
          newName = input(f'New name (leave blank to keep current): ').strip() or contact['name']
          newEmail = input(f'New email address (leave blank to keep current): ').strip() or contact['email']

          if len(newPhoneNumber) != 9:
            print(f'Invalid phone number {newPhoneNumber}')
            return

          # Add the updated contact into the list
          contact['phoneNumber'] = newPhoneNumber
          contact['name'] = newName
          contact['email'] = newEmail

          clearScreen()
          print('Updating ...')
          clearScreen()
          sleep(1.2)
          print(f'Update sucessufully! [{contact['phoneNumber']}] {contact['name']} - {contact['email']}\n')
          sleep(0.4)
          clearScreen()
        
        else:
          print(f'Invalid phone number "{phoneNumberToUpdate}"! Please, try again.\n')

    except ValueError as error:
      print(f'Error: Invalid value {error}! Please, try again.\n')


def searchContact():
    if not contactList:
      print('Contact list is empty!\n')
      return

    try:
      phoneNumberToSearch = input('Enter the phone number to search: ').strip()

      for contact in contactList:

        if phoneNumberToSearch == contact['phoneNumber']:
          print(f'Contact found: Name: {contact['name']}, Phone: {contact['phoneNumber']}, Email: {contact['email']}')
        
      add = input(f'\n"{phoneNumberToSearch}" not found! Do you want to add a new contact? (Y/N): ').lower()
      if add == 'y':
        name = input('Enter the name: ')
        email = input('Enter the email address: ')
        contactList.append({'phoneNumber': phoneNumberToSearch, 'name': name, 'email': email})
      else:
        print(f'"{phoneNumberToSearch}" not added.\n')
       
    except ValueError as error:
      print(f'Error: Invalid value {error}! Please, try again.\n')
    

def main():
    print('\nWelcome to Contact Book')

    while True:
      print('\n1. to add a new contact')
      print('2. to view contact list')
      print('3. to delete acontact')
      print('4. to update a contact')
      print('5. to search a contact')
      print('6. to leave the program')

      option = userOption()
      clearScreen()

      if option == 1:
        addContact()
      elif option == 2:
        viewContactList()
      elif option == 3:
        deleteContact()
      elif option == 4:
        updateContact()
      elif option == 5:
        searchContact()
      elif option == 6:
        print('Goodbye!')
        break


if __name__ == "__main__":
    main()