def userInput():
    try:
      text = input('Write something: ').strip()
      return text
    except ValueError:
      print('Invalid value! Please, try again.')


def convertText(text):
  try:
    textConverted = text.replace(' ', '...')
    return textConverted
  except ValueError:
    print('Invalid value! Please, try again.')


def main():
    text = userInput()
    convertedText = convertText(text)
    print(f'\n {convertedText}')

if __name__ == "__main__":
    main()