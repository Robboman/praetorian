import requests

# API base URL
base_url = "http://crypto.praetorian.com/challenge/"

# Challenge level
level = "<#>"
challenge_url = f"{base_url}{level}/"

# Auth token
token = "<token_here>"

# Guess/keyword
guess_payload = {
    "guess": "<guess>"
}

# Headers
headers = {
    "Authorization": f"JWT {token}",
    "Content-Type": "application/json"
}

# POST request
response = requests.post(challenge_url, json=guess_payload, headers=headers)

# Response check
if response.status_code == 200:
    data = response.json()
    hash_value = data.get("hash")
    if hash_value:
        print(f"Correct guess! Hash: {hash_value}")
    else:
        print("No hash found in the response.")
else:
    print(f"Error: Unable to solve challenge. Status code: {response.status_code}")
    print(response.json())
