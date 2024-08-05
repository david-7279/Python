def gel_valid_input():
    while True:
      camelCase = input('camelCase: ').strip()
      if camelCase:
        return camelCase
      else:
        print('Invalid input! Please, try again.\n')


def convert_camelCase_to_snakeCase(camel):
    snake_case = ""
    for i in camel:
      if i.isupper():
        snake_case += '_' + i.lower()
      else:
        snake_case += i
    return snake_case
      

def main():
    camelCase = gel_valid_input()
    convert = convert_camelCase_to_snakeCase(camelCase)
    print(convert)


if __name__ == "__main__":
    main()