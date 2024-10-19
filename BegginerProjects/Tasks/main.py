from task import Task
import os
from time import sleep

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(1)

# Verify the menu choices
def user_choice():
  choices = [1, 2, 3, 4, 5, 6, 7, 0]
  while True:
    try:
      choice = int(input('Choose an option: '))
      if choice in choices:
        return choice
      else:
        print(f'Invalid choice: {choice}. Please, try again.')
    except ValueError:
      print('Invalid number! Please, try again.') 

# Main program
def main():
  print('Welcome to the Task Manager.\nHere you can create your daily tasks.\n')

  task_manager = Task()

  while True:  # Loop for the menu
    print('1. Add task')
    print('2. View tasks')
    print('3. View tasks by category')
    print('4. Update task')
    print('5. Remove task')
    print('6. Remove all task')
    print('7. Save task in the file')
    print('0. Exit')

    choice = user_choice()
    clear_screen()

    if choice == 1:
      task_manager.create_task()
    elif choice == 2:
      task_manager.view_task()
    elif choice == 3:
      task_manager.view_task_by_category()
    elif choice == 4:
      task_manager.update_task()
    elif choice == 5:
      task_manager.remove_task()
    elif choice == 6:
      task_manager.remove_all_task()
    elif choice == 7:
      task_manager.save_tasks_to_file()
    elif choice == 0:
      print('Goodbye!')
      break 

# Call principal program
if __name__ == '__main__':
  main()