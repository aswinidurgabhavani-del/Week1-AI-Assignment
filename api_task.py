import requests

url = "https://official-joke-api.appspot.com/random_joke"

try:
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    print("\n============😂 RANDOM JOKE===========")
    print("Setup :", data["setup"])
    print("Punchline :", data["punchline"])
    print("Type :", data["type"])
    print("=======================================\n")

except requests.exceptions.RequestException as e:
    print("Error:", e)