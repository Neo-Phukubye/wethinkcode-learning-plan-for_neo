def main():
    weight=int(input("weight(in kg): "))
    energy=einstein(weight)
    print(f"Energy: {energy}")

def einstein(m):
    c=300000000
    return m*c**2

main()
