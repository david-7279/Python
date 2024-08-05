def userInput():
    text = input('Write old emojis to convert them: ').strip()
    if text == '':
        print('No input provided. Please, try again.')
        return None
    return text

def convertText(text):
    conversions = {
        ':)': '🙂',
        ':(': '🙁',
        ':D': '😃',
        'XD': '😆',
        ';)': '😉'
    }

    for oldEmoji, newEmoji in conversions.items():
      text = text.replace(oldEmoji, newEmoji)

    return text

def main():
    text = userInput()
    if text is not None:
        convertedText = convertText(text)
        print(f'\n{convertedText}')
    else:
        print('No valid input to convert! Please, try again.')

if __name__ == "__main__":
    main()
