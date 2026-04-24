import requests

BOT_TOKEN = "8685078633:AAGD5YwBE1u5Ii1kPwB9rZ6Jp4tNDdv57NU"
CHAT_ID = "38908105"

url = f"https://api.telegram.org/bot{8685078633:AAGD5YwBE1u5Ii1kPwB9rZ6Jp4tNDdv57NU}/sendMessage"

r = requests.post(
    url,
    json={"chat_id": CHAT_ID, "text": "ТЕСТ 🚀"},
    timeout=20
)

print("STATUS:", r.status_code)
print("RESPONSE:", r.text)
