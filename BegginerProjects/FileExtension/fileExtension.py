def userInput():
    fileName = input('File name: ').strip().lower()
    if fileName != '':
      return fileName
    else:
      print('Invalid file name! Please, try again.\n')
      return None


def verifyExtension(extension): 
    """
    file[0]: The part of the string before the last dot.
    file[1]: The dot itself.
    file[2]: The part of the string after the last dot (the file extension)
    """

    file = extension.rpartition('.')  

    match file[2]:
      case 'gif' | 'jpeg' | 'png':
        print(f'image/{file[2]}')
        return
      case 'jpg':
        print('image/jpeg')
        return
      case 'pdf' | 'zip' | 'doc':
        print(f'application/{file[2]}')
      case 'txt':
        print('text/plain')
      case _:
        print('application/octet-stream')
      


def main():
  extension = None

  while extension is None:
    extension = userInput()
  
  verify = verifyExtension(extension)


if __name__ == "__main__":
    main()