import random, string, os
from specialCharacters import specialCharacters
from time import sleep


def clearScreen():
    os.system('cls')
    sleep(1)


def lenghtPassword(password):
    if 8 <= len(password) <= 32:
      print(f'Password valid!')
      return len(password)
    else:
      print(f'Password invalid! Enter a password with 8 to 32 characters.')
      return False


def specialCharacter(passwordLength):
    specialChar = []
    # 1. Generate random characters based on 60% lenght the password
    numSpecial = int(0.6 * passwordLength)
    # 2. Append the special character into a list
    for _ in range(numSpecial):
      specialChar.append(random.choice(specialCharacters))
    # 2. Return all characters
    return specialChar


def lowerUpperLetter(passwordLength):
    letters = []
    # 1. Generate random letter based on 40% lenght the password
    numUpper = numLower = int(0.2 * passwordLength)

    # 2. Append the upper and lower letter into a list
    for _ in range(numUpper):
      letters.append(random.choice(string.ascii_uppercase))

    for _ in range(numLower):
      letters.append(random.choice(string.ascii_lowercase))
    
    # 3. Return all letters
    return letters


def combineAndShuffle(originalPassword, specialChars, letters):
    # 1. Create a variable to store combine special character with upper and lower letters
    combine = list(originalPassword) + specialChars + letters
    # 2. Shuffle the combine special character with upper and lower letter
    random.shuffle(combine)
    # 3. Store the combine shuffle into finalPassword
    finalPassword = ''.join(combine)
    # 4. Return the final password
    return finalPassword


def main():
    print("Welcome to Passowrd Generator!")
    print('')

    password = input("Enter your password: ")
    newPassword = lenghtPassword(password)

    # Verify the password is valid
    if newPassword:
      # Generate specialCharacters based on password
      specialChars = specialCharacter(newPassword)
      # Generate upperLower letter based on password
      upperLower = lowerUpperLetter(newPassword)
      # Combine the password
      clearScreen()
      print('\nCombining password ....')
      sleep(1.5)

      # Print the password
      clearScreen()
      finalPassword = combineAndShuffle(password, specialChars, upperLower)
      print(f'\nNew Password: {finalPassword}')

if __name__ == "__main__":
  main()