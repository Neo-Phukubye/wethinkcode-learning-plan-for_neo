def convert(str):
    str=str.replace(":)", "🙂")
    str=str.replace(":(", "🙁")
    return str

def main():
    user_input=input("Input: ")
    print(convert(user_input))

main()
