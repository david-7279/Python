def get_valid_input():
    while True:
      text = input('Input: ')
      if text:
        return text
      else:
        print('Invalid input! Please, try again.')


def remove_vowels(text):
    output_text = ""
    vowels = 'aeiouAEIOU'

    for char in text:
      if char not in vowels:
        output_text += char
      
    return output_text


def main():
    text = get_valid_input()
    removed_text = remove_vowels(text)
    print(f'Output: {removed_text}')


if __name__ == "__main__":
    main()