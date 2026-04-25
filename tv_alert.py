print("START SCRIPT")

import requests

BOT_TOKEN = "8685078633:AAF46dqI3-SWkUWDEQb21yb8YPfgm4VfpUA"
CHAT_ID = "38908105"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    json={"chat_id": CHAT_ID, "text": "ТЕСТ 🚀"},
    timeout=20
)

print("STATUS:", r.status_code)
print("RESPONSE:", r.text)
