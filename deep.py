def main():
    result=input("What is the result to the great question of life,the universe, and everything?").strip().lower()

    if result=="42" or result=="forty-two" or result=="forty two":
        print("yes")
    else:
        print("no")

main()
