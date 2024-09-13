import requests

# API base URL
auth_url = "http://crypto.praetorian.com/api-token-auth/"

# Email
email = {"email": "<enter email>"}

# POST request for JWT token
response = requests.post(auth_url, json=email)

# Response check
if response.status_code == 200:
    token = response.json().get("token")
    if token:
        print(f"Authentication successful. Token: {token}")
    else:
        print("Token not found in response.")
else:
    print(f"Authentication failed. Status code: {response.status_code}")
    print(response.json())
