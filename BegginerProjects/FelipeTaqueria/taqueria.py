def get_valid_item():
    menu = item_dictionary()
    total_cost = 0.0
    while True:
      try:
        item = input('Item: ').title().strip()
        if item in menu:
          total_cost += menu[item]
          print(f'Total: ${total_cost:.2f}')
        else:
          print('Invalid item! Please, try again.')
      except EOFError:
        print() # New line
        break
    return total_cost


def item_dictionary():
    return {
      "Baja Taco": 4.25,
      "Burrito": 7.50,
      "Bowl": 8.50,
      "Nachos": 11.00,
      "Quesadilla": 8.50,
      "Super Burrito": 8.50,
      "Super Quesadilla": 9.50,
      "Taco": 3.00,
      "Tortilla Salad": 8.00
    }


def main():
    total_cost = get_valid_item()
    print(f'Final total: {total_cost:.2f}')
    

if __name__ == "__main__":
    main()