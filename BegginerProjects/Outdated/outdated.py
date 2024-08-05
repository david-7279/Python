months = {
    "january": "01", 
    "february": "02", 
    "march": "03", 
    "april": "04", 
    "may": "05",
    "june": "06", 
    "july": "07", 
    "august": "08", 
    "september": "09", 
    "october": "10",
    "november": "11", 
    "december": "12"
}

def get_valid_date():
    while True:
        try:
            date = input('Date: ').strip()

            # Check if MM/DD/YYYY format
            if '/' in date:
                parts = date.split('/')
                if len(parts) == 3:
                    month, day, year = parts
                    if verify_date(month, day, year):
                        return convert_date(year, month, day)

            # Check if Month DD, YYYY format
            elif ',' in date:
                parts = date.split(' ')
                if len(parts) == 3:
                    month_name = parts[0].lower()
                    day = parts[1].strip(',')
                    year = parts[2].strip()
                    if month_name in months and verify_date(months[month_name], day, year):
                        return convert_date(year, months[month_name], day)

        except EOFError:
            break
        except ValueError:
            pass

def verify_date(month, day, year):
    try:
        month = int(month)
        day = int(day)
        year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except ValueError:
        pass
    return False

def convert_date(year, month, day):
    return f"{int(year):04}-{int(month):02}-{int(day):02}"

def main():
    while True:
        date = get_valid_date()
        if date:
            print(date)
            break

if __name__ == "__main__":
    main()