from pathlib import Path
import requests
from decouple import config


SPITCH_API_KEY = config("SPITCH_API_KEY")


url = "https://api.spi-tch.com/v1/transcriptions"


payload = {
    "language": "yo",
}

headers = {
    "Authorization": f"Bearer {SPITCH_API_KEY}",
}


with open('/home/iyanuashiri/Software/Python/spitch-project/app/audio.wav', 'rb') as f:
    files = {"content": f}
    response = requests.post(url, data=payload, files=files, headers=headers)
    print(response.json())
    
# {'request_id': '5846f4ea-041b-4402-b14a-181273b7539c', 'text': 'Báwo ni olólùfẹ́, ìfẹ́ Olúwa, bí mi Olúwa, ìyàn mú Olúwa, ìfẹ́ Olúwa?'}    

# {'request_id': '33ec5d08-2ecf-4db7-88a8-1d48260db221', 'text': 'Báwo ni olólùfẹ́, ìfẹ́ Olúwa, bí mi Olúwa, ìyàn mú Olúwa?'}

# {'request_id': 'a40fa5f4-7f00-4e1a-8795-e1f171826db3', 'text': 'Báwo ni olólùfẹ́? Ìfẹ́ Olúwa bí mi Olúwa ìyànwó Olúwa?'}

# {'request_id': 'a7690c28-1966-4072-8c69-ff984ab07447', 'text': 'Báwo ni olólùfẹ́?'}