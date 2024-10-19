import os
from time import sleep

# Clear the terminal
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  sleep(1)

 
task_list = []

category_task = {
  "Education": 'e',
  "Work": 'w',
  "House": 'h',
  "Personal": 'p',
  "Coding": 'c'
}

# Task class - Add, remove, view, and edit task
class Task:
  def __init__(self):
    pass


  def create_task(self):
    name = input('Enter the task name: ')
    print('\nCategories: ')
    for cat, key in category_task.items():
      print(f'- {cat}: {key}')

    while True:
      try:
        category = input('Enter the category: ').lower()
        if category in category_task.values():
          task_list.append({'name': name, 'category': category})
          print('\nTask added sucessfully!')
          sleep(0.7)
          clear_screen()
          return
        else:
          print(f'Invalid category task: {category}. Please, try again.')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')
  

  def view_task(self):
    if not task_list:
      print('No task available.\n')
      return
    
    print('Your tasks: ')
    for index, task in enumerate(task_list, start=1):
      category_name = [cat for cat, key in category_task.items() if key == task['category']]
      if category_name:
        print(f'[{index}] Task name: {task['name']} - Category: {category_name[0]}')
    print('')


  def view_task_by_category(self):
    if not task_list:
      print('No task available.\n')
      return

    print('Categories: ')
    for cat, key in category_task.items():
      print(f'- {cat}: {key}')
    
    while True:
      try:
        category_input = input('Select the category: ').lower()
        if category_input in category_task.values():
          found = False  # Flag to check if tasks are found in the category

          clear_screen()
          category_name = [cat for cat, key in category_task.items() if key == category_input]
          print(f'Tasks in category: {category_name}')

          for task in task_list:
            if task['category'] == category_input:
              category_name = [cat for cat, key in category_task.items() if key == task['category']]
              print(f'- Task name: {task["name"]}')
              found = True  # Task found, set flag to True
          print('')
          if not found:
              print(f'No tasks available in this category.\n')
          return  # Exit after processing the category

        else:
          print(f'Invalid category: {category_input}. Please, try again.\n')

      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.\n')

  def update_task(self):
    if not task_list:
      print('No task available.')
      return
    
    print('Your task: ')
    for index, task in enumerate(task_list, start=1):
      category_name = [cat for cat, key in category_task.items() if key == task['category']]
      print(f'[{index}] Task name: {task['name']} - Category: {category_name[0]}')
    print(f'[0] To leave.\n')

    while True:
      try:
        task_index = int(input('Choose a task to remove by its index: '))
        
        if 1 <= task_index <= len(task_list):
          selected_task = task_list[task_index - 1]
          print(f'Update the task: {selected_task['name']}')

          new_name = input('New name of the task (Leave Blank to keep the name): ') or selected_task['name']

          print('\nCategories: ')
          for cat, key in category_task.items():
            print(f'- {cat}: {key}')
          new_category = input('New category of the task (Leave Blank to keep the name): ') or selected_task['category']

          if new_category in category_task.values():
            if new_name != selected_task['name'] or new_category != selected_task['category']:
              selected_task['name'] = new_name
              selected_task['category'] = new_category
              print('Task updated sucessfully!\n')
              self.save_tasks_to_file()
              return
            else:
              print('No changes made. Task remains the same.\n')
          else:
            print(f'Invalid category: {new_category}. Please, try again.\n')

        elif task_index == 0:
          print('No changes made. All tasks remain the same.\n')
          return
        else:
          print(f'Invalid index: {task_index}. Please, try again.')

      except ValueError:
        print('Please enter an valid number for the index.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.')

  ## IMPLEMENTS TO EXIT FOR NOT TO REMOVE ANY TASK AT ALL
  def remove_task(self):
    if not task_list:
      print('No task available. \n')
      return
    
    print('Your task: ')
    for index, task in enumerate(task_list, start=1):
      category_name = [cat for cat, key in category_task.items() if key == task['category']]
      print(f'[{index}] Task name: {task['name']} - Category: {category_name[0]}')
    print(f'[0] To leave.\n')

    while True:
      try:
        task_index = int(input('Choose a task to remove by its index: '))
        if 1 <= task_index <= len(task_list):
          removed_task = task_list.pop(task_index - 1) 
          print(f'Task removed sucessfully: [{task_index}] {removed_task['name']}\n')
          return
        elif task_index == 0:
          print('No changes made. All tasks remain the same.\n')
          return
        else:
          print(f'Invalid index: {task_index}. Please, try again.\n')
      except ValueError:
        print('Please enter an valid number for the index.\n')
      except Exception as e:
        print(f'An error ocurred: {e}. Please, try again.\n')

    
  def remove_all_task(self):
    if not task_list:
      print('No tasks available.')
      return
    
    while True:
      try:
        confirmation = input('Are you sure you want to remove all the tasks (Yes/No)? ').lower()
        if confirmation == 'y' or confirmation == 'yes':
          task_list.clear()
          print('All tasks have been removed successfully!\n')
          return
        elif confirmation == 'n' or confirmation == 'no':
          print('No changes made. All tasks remain the same.\n')
          return
        else:
          print(f'Invalid confirmation: {confirmation}. Please, try again.')
      except Exception as e:
        print(f'An error occurred: {e}. Please, try again.')


  
  def save_tasks_to_file(self, filename='Tasks.txt'):
    try:
        # Dicionário para armazenar tarefas agrupadas por categoria
        tasks_by_category = {key: [] for key in category_task.values()}

        # Agrupa as tarefas por categoria
        for task in task_list:
            tasks_by_category[task['category']].append(task['name'])

        with open(filename, 'w') as file:
            for category_code, tasks in sorted(tasks_by_category.items()):
                if tasks:  # Verifica se há tarefas nesta categoria
                    # Obtém o nome da categoria correspondente
                    category_name = [cat for cat, key in category_task.items() if key == category_code]
                    if category_name:
                        file.write(f'[{category_name[0]}]\n')  # Escreve o nome da categoria
                        for task_name in sorted(tasks):  # Ordena as tarefas alfabeticamente
                            file.write(f'   - {task_name}\n')  # Escreve a tarefa
                        file.write('\n')  # Adiciona uma linha em branco entre as categorias

        print('Tasks saved to file successfully!\n')
    except Exception as e:
        print(f'An error occurred while saving tasks: {e}. Please try again.')

