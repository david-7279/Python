def get_valid_fruits():
    while True:
      fruit = input('Item: ').lower().strip()
      if fruit:
        return fruit
      else:
        print(f'Invalid fruit {fruit}! Please, try again.')


def calories_of_fruit(fruit):
    fruit_list = {
      'apple' : 130,
      'avocado': 50,
      'banana': 110,
      'cantaloupe': 50,
      'grapefuit': 60,
      'grapes': 90,
      'honey melon': 50,
      'kiwifruit': 90,
      'lemon': 15,
      'lime': 20,
      'nectarine': 60,
      'orange': 80,
      'peach': 60,
      'pear': 100,
      'pineapple': 50,
      'plums': 70,
      'strawberries': 50,
      'sweet cherries': 100,
      'tangerine': 50,
      'watermelon': 80,
    }      
    return fruit_list.get(fruit)


def main():
    while True:
      fruit = get_valid_fruits()
      calories = calories_of_fruit(fruit)
      if calories is None:
        print(f'Invalid fruit "{fruit}"! Please, try again.')
        return
      else:
        print(f'Calories: {calories}')
        break


if __name__ == "__main__":
    main()