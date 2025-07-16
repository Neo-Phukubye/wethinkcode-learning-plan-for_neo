def main():
    plate= input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not(2 <= len(s) <= 6):
        return False

    if not(s[:2].isalpha()):
        return False

    if not s.isalnum():
        return False

    digit_found= False

    for i in range(len(s)):
        if s[i].isdigit():
            if not digit_found:
               if s[i] == '0':
                  return False

            digit_found = True
        elif digit_found:
           return False

    return True

if __name__ == "__main__":
        main()
