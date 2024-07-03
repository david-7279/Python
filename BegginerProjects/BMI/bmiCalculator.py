import os
from time import sleep


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    sleep(1)


def weightMeasurements():
    try:
      weight = int(input('Choose an option: '))
      if weight == 1:
        return 'kg'
      elif weight == 2:
        return 'lbs'
      else:
        print(f'Invalid option {weight}! Please, try again.')
        return False
        return weightMeasurements()
    except ValueError:
      print(f'Invalid number {weight}! Please, try again')
      return weightMeasurements()


def heightMeasurements():
    try:
      height = int(input('Choose an option: '))
      if height == 1:
        return 'cm'
      elif height == 2:
        return 'ft'
      else:
        print(f'Invalid option {height}! Please, try again.')
        return heightMeasurements()
    except ValueError:
      print(f'Invalid number {height}! Please, try again')
      return heightMeasurements()


def genderSelection():
    gender = input('Choose an option: ').upper()
    if gender == 'M':
      return 'Male'
    elif gender == 'F':
      return 'Female'
    else:
      print(f'Invalid option {gender}! Please, try again.')
      return genderSelection()


def weightConversion(weight):
    # Convert lbs to kg
    return weight * 0.453592


def heightConversion(height):
    # Convert ft to cm
    return height * 30.48


def BMICalculator(weight, height):
    height /= 100  # Convert cm to meters
    return weight / (height ** 2)


def classification(BMI):
    if BMI < 18.5:
      return 'underweight'
    elif 18.5 <= BMI < 24.9:
      return 'normal weight'
    elif 25 <= BMI < 29.9:
      return 'overweight'
    elif BMI >= 30:
      return 'obesity'
    else:
      return 'Invalid measurments!'
    


def main():
    clearScreen()
    print("Welcome to IBM calculator")
    print('')

    print('Select your weight measurment')
    print('1. for Kilogram (kg)')
    print('2. for pound (lbs)')
    weightUnit = weightMeasurements()
    clearScreen()

    print('Select your height measurment')
    print('1. for centimeters (cm)')
    print('2. for feet (ft)')
    heightUnit  = heightMeasurements()
    clearScreen()

    print('Select your gender')
    print('M. for male')
    print('F. for female')
    genderUnit  = genderSelection()
    clearScreen()

    weight = float(input(f'Weight ({weightUnit}): '))
    height = float(input(f'Height ({heightUnit}): '))
    age = int(input('Age: '))

    if weightUnit == 'lbs':
      weight = weightConversion(weight)
    
    if heightUnit == 'ft':
      height = heightConversion(height)

    # Calculates the BMI
    BMI = BMICalculator(weight, height)
    # Classify BMI
    category = classification(BMI)

    clearScreen()
    print('Your data')
    print(f'weight: {weight:.2f} ({weightUnit})')
    print(f'height: {height:.2f} ({heightUnit})')
    print(f'gender: {genderUnit}')  
    print(f'age: {age}')
    print('')

    # Display results
    print('Calculating your BMI ...')
    sleep(2)
    print(f'\nYour BMI is {BMI:.2f}, which is considered {category}.')


if __name__ == "__main__":
  main()