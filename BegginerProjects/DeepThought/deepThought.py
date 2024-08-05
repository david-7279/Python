def userInput():
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').strip().lower()
    if answer is None:
      print(f'Invalid answer {answer}! Please, try again.')
      return None
    else:
      return answer



def verifyAnswer(answer):
    if (answer == '42') or (answer == 'forty-two') or (answer == 'forty two'):
      return 'Yes'
    else:
      return 'No'


def main():
  answer = None

  while answer is None:
    answer = userInput()

  verify = verifyAnswer(answer)
  print(f'{verify}')


if __name__ == "__main__":
    main()