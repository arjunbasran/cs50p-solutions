import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Must have one value for quantity of Bitcoin in command-line argument")

    try:
        bitcoins = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument must be a number")

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e21ca337e51d661fbeed576127342c3671daefe37a6b56d516da13503b0ea65a")
        response.raise_for_status()

    except requests.RequestException:
        sys.exit("Request failed")

    content = response.json()

    price = float(content["data"]["priceUsd"]) * bitcoins

    print(f"${price:,.4f}")

if __name__ == "__main__":
    main()
















