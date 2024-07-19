import os
from time import sleep

# Global array for grades
grades = []

def clearScreen():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')


def userOption():
    choices = [1, 2, 3, 4, 5]
    while True:
      try:
        option = int(input('Choose an option: '))
        if option in choices:
          return option
        else:
          print(f'Invalid option {option}! Please, try again.')
      except ValueError as error:
        print(f'Error: {error}! Please, try again.')


def insertGrades():
    student = input('Student name: ').strip()
    subject = input('Subject name: ').strip()
    try:
      grade = float(input(f'{student} grade (0-20): '))
      if 0 <= grade <= 20:
        print(f'{student} [{subject}]: {grade}, added sucessufully!')
        grades.append({'student': student, 'subject': subject, 'grade': grade})
        sleep(0.3)
        clearScreen()
      else:
        print(f'Invalid grade {grade}! Please, try again.')
    except ValueError as error:
      print(f'Error: {error}! Please, try again.')


def highestLowestGrades():
    clearScreen()
    print('Checking for grades ... ')
    sleep(1.5)
    clearScreen()

    if not grades:
      print('No grades in the list!\n')
      return

    highestGrade = max(grades, key=lambda x: x['grade'])
    lowestGrade = min(grades, key=lambda x: x['grade'])

    print('Calculating highest and lowest grades ...')
    sleep(1.3)
    clearScreen()
    print(f'Highest grade is: {highestGrade['grade']} by {highestGrade['student']} in the {highestGrade['subject']}!')   
    print(f'Lowest grade is: {lowestGrade['grade']} by {lowestGrade['student']} in the {lowestGrade['subject']}!') 


def averageGrades():
    clearScreen()
    print('Checking for grades ... ')
    sleep(1.5)
    clearScreen()

    if not grades:
      print('No grades in the list!\n')
      return

    gradesSum = sum(entry['grade'] for entry in grades)
    gradesCount = len(grades)
    average = gradesSum / gradesCount

    print('Calculating the average grades ...')
    sleep(1.3)
    clearScreen()
    print(f'Average grade is: {average}')   


def passedStudents():
    clearScreen()
    print('Checking for grades ... ')
    sleep(1.5)
    clearScreen()

    if not grades:
      print('No grades in the list!\n')
      return

    countPassedStudents = 0
    studentsPassed = []

    for entry in grades:
      grade = entry['grade']
      student = entry['student']
      subject = entry['subject']

      if 10 <= grade <= 20:
        print(f'{student} passed with {grade} in {subject}')
        countPassedStudents += 1
        studentsPassed.append(student)
      elif 0 <= grade <= 9.4:
        print(f'{student} failed with {grade} in {subject}')
      else:
        print(f'Invalid grade {grade}!')

    if countPassedStudents > 0:
      print(f'\nNumber of passed studnets: {countPassedStudents}')
      for student in studentsPassed:
        print(f'Student {student} passed!')
    else:
      print('All students failed')


def main():
    clearScreen()
    print('Welcome to Grade Calculator!')

    while True:
      print('')
      print('1. to insert grades')
      print('2. to highest and lowest grades')
      print('3. to average grades')
      print('4. to numbers of students who passed')
      print('5. to leave the program\n')
      
      option = userOption()
      clearScreen()

      if option == 1:
        insertGrades()
      elif option == 2:
        highestLowestGrades()
      elif option == 3:
        averageGrades()
      elif option == 4:
        passedStudents()
      elif option == 5:
        print('Goodbye!')
        break

if __name__ == "__main__":
    main()