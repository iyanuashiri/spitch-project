import requests
from decouple import config


SPITCH_API_KEY = config("SPITCH_API_KEY")


url = "https://api.spi-tch.com/v1/speech"

payload = {
    "text": "Báwo ni olólùfé? Ìfẹ́olúwa. Bímiólúwa. Ìyànúolúwa. Ìfẹ́olúwa.",
    "voice": "sade",
    "language": "yo"
}
headers = {
    "Authorization": f"Bearer {SPITCH_API_KEY}",
    "Content-Type": "application/json"
}

with open("audio5.wav", "wb") as f:
    response = requests.request("POST", url, json=payload, headers=headers)
    f.write(response.content)

# response.json()