def get_valid_item():
    grocery_list = {}
    while True:
      try:
        item = input().strip().lower()
        if item in grocery_list:
          grocery_list[item] += 1
        else:
          grocery_list[item] = 1
      except EOFError:
        print()
        break
    return grocery_list


def print_grocery_list(grocery_list):
    count = 0
    for item in sorted(grocery_list):
      print(f'{grocery_list[item]} {item.upper()}')
  

def main():
    grocery_list = get_valid_item()
    grocery = print_grocery_list(grocery_list)


if __name__ == "__main__":
    main()