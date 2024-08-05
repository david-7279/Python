def is_valid(s):
    # Length check: Ensure length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check if it starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Ensure all characters are alphanumeric
    if not s.isalnum():
        return False

    # Ensure all digits are at the end and no letters appear after the first digit
    digit_started = False
    for char in s:
        if char.isdigit():
            digit_started = True
        elif digit_started and char.isalpha():
            return False

    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()