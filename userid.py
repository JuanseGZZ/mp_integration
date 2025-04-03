import requests

import varibale

ACCESS_TOKEN = varibale.TOKEN
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get("https://api.mercadopago.com/users/me", headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(f"🆔 Tu user_id es: {user_data['id']}")
else:
    print("❌ Error al obtener user_id:", response.text)
