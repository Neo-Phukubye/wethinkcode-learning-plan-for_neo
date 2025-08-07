import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        response = requests.get("https://api.coincap.io/v3/assets/bitcoin")
        response.raise_for_status()
        data = response.json()
        rate = float(data["data"]["priceUsd"])
        amount = n * rate
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("Request failed")

if __name__ == "__main__":
    main()