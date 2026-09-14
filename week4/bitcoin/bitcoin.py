import sys
import requests
#add your API key before executing it
try:
    n = float(sys.argv[1])
    data = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=")
    formatted_data = data.json()
    price = float(formatted_data["data"]["priceUsd"])
    print(f"${price * n:,.4f}")
except requests.RequestException:
    sys.exit()
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
    