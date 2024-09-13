import requests

# API base URL
base_url = "http://crypto.praetorian.com/challenge/"

# Challenge level
level = "<#>"
challenge_url = f"{base_url}{level}/"

# Auth token
token = "<token_here>"

# Headers
headers = {
    "Authorization": f"JWT {token}"
}

# GET request
response = requests.get(challenge_url, headers=headers)

# Response check
if response.status_code == 200:
    data = response.json()
    print(f"Level: {data['level']}")
    print(f"Challenge: {data['challenge']}")
    print(f"Hint: {data['hint']}")
else:
    print(f"Error: Unable to retrieve challenge. Status code: {response.status_code}")
    print(response.json())
