def getValidTime():
    while True:
      time = input('What time is it? ').strip()
      if time and validateTimeFormat(time):
        return time
      else:
        print('Invalid time! Please, try again.')


def validateTimeFormat(time):
    parts = time.split(':')
    if len(parts) != 2:
      return False
    
    hours, minutes = parts
    if not (hours.isdigit()) and (minutes.isdigit()):
      return False

    hours = int(hours)
    minutes = int(minutes)

    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
      return False
    return True 


def convertTime(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60.0


def main():
    time = getValidTime()
    time_in_hours = convertTime(time)
    
    if 7 <= time_in_hours <= 8:
      print('Breakfast time')
    elif 12 <= time_in_hours <= 13:
      print('Lunch time')
    elif 18 <= time_in_hours <= 19:
      print('Dinner time')


if __name__ == "__main__":
    main()