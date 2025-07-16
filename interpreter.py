def main():
    expressions=input("Expressions: ")
    x, operator, z = expressions.strip().split()

    x= float(x)
    z= float(z)

    if operator == "+":
        result=x + z
    elif operator == "-":
        result=x - z
    elif operator == "*":
        result=x * z
    elif operator == "/":
       result =x / z

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
