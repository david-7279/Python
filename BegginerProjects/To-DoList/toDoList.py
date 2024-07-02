import os
from time import sleep

def clearScreen():
    sleep(1.2)
    os.system('cls')
    os.system('cls')


def strikeThrough(text):
    return ''.join([char] + '\u0336' for char in text)


def taskInput():
    choices = [1, 2, 3 ,4 ,5]
   
    # 1. Check if the option is valid
    while True:
      try:
        option = int(input('Choose an option: '))
        if option in choices:
          return option
        else:
           print(f'Invalid option [{option}]! Please try again.')
      except ValueError:
         print(f'That\'s not a valid number [{option}]! Please try again.')


def addTask(tasks):
    # 1. Write a new task
    newTask = input('Enter the new task: ')
    # 2. Check if the task at least have 2 letters
    if len(newTask) >= 2:
    # 3. Add a new task in the task list
      tasks.append(newTask)
      print(f'Task: "{newTask}" added suscessfully!')
      return True
    else:
      print(f'Task: "{newTask}" should have at least 2 characters! Task not added')
      return False


def viewTask(task):
    # 1. Print the task list
    if not task:
      print('Task list empty!')
    else:
      print('Tasks: ')
      # 2. Iterate the list
      i = 1
      for i, task in enumerate(task):
        print(f'[{i + 1}] {task}')


def markTaskCompleted(tasks):
    # 1. Verify if the task is empty
    if not tasks:
      print('Task list empty!')
      return False
    else:
      # 2. Print the task list
      print('Tasks: ')
      # 3. Iterate the task list
      i = 1
      for i, task in enumerate(tasks):
        print(f'[{i + 1}] {task}')
      # 4. Select the task to mark as completed
      selectedTask = int(input('Choose an task to mark as completed: ')) - 1
      # 3. Verify the task exists, and mark the task as completed
      if 0 <= selectedTask < len(tasks):
        completedTask = tasks[selectedTask]
        print(f'Mark task "{completedTask}" as completed!')
        return True
      else:
        print(f'Invalid task "{selectedTask}"! Please choose a valid task.')
        return False


def deleteTask(tasks):
    # 1. Verify if the task is empty
    if not tasks:
      print('Task list empty')
      return False
    else:
      # 2. Print the task list
      print('Tasks: ')
      # 3. Iterate the task list
      i = 1
      for i, task in enumerate(tasks):
        print(f'[{i + 1}] {task}')

      try:
        # 4. Select the task to remove
        selectedTask = int(input('Choose an task to remove: ')) - 1
        # 5. Verify the task exists, and remove the task
        if 0 <= selectedTask < len(tasks):
          removeTask = tasks.pop(selectedTask)
          print(f'Task: [{selectedTask + 1}] removed successfully!')
          return True
        else:
          print(f'Invalid task [{selectedTask + 1}]! Please choose a valid task.')
          return False
      except ValueError:
        print(f'Invalid input [{selectedTask}]! Please choose a valid number.')
        return False


def main():
    tasks = []
    print('Welcome to the To-Do List Application!')
     
    while True:
      print('\n1. Add Task')
      print('2. View Tasks')
      print('3. Mark Task as Completed')
      print('4. Delete Task')
      print('5. Exit\n')
      option = taskInput()  
        
      if option == 1:
        addTask(tasks)
        clearScreen()
      elif option == 2:
        clearScreen()
        viewTask(tasks)
      elif option == 3:
        clearScreen()
        markTaskCompleted(tasks)
        clearScreen()
      elif option == 4:
        clearScreen()
        deleteTask(tasks)
        clearScreen()
      elif option == 5:
        print('Exiting the To-Do List Application. Goodbye!')
        break
      else:
        print(f'Invalid option {option}! Please choose a valid option.')
        clearScreen()


if __name__ == "__main__":
    main()