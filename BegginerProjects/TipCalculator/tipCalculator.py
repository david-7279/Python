def dollarsToFloat(dollars):
    try:
      # Remove the '$' sign if present and strip any whitespace
      dollars = dollars.replace('$', '').strip()
      return float(dollars) # Convert to float
    except ValueError:
      print('Invalid value! Please, try again.')
      return None


def percentToFloat(percent):
    try:
      # Remove the '%' sign if present and strip any whitespace
      percent = percent.replace('%', '').strip()
      return float(percent) / 100 # Convert to float and divide by 100 to get the percentage value
    except ValueError:
      print('Invalid value! Please, try again.')
      return None


def main():
    dollars = None
    percent = None

    while dollars is None:
      dollars = dollarsToFloat(input("How much was the meal? "))
    while percent is None:
      percent = percentToFloat(input("What percentage would you like to tip? "))

    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


if __name__ == "__main__":
    main()