import requests

import varibale  

ACCESS_TOKEN = varibale.TOKEN  
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get("https://api.mercadopago.com/pos", headers=headers)

if response.status_code == 200:
    data = response.json()
    if "results" in data:
        for pos in data["results"]:
            print(f"👉 POS Name: {pos.get('name')}")
            print(f"🔑 POS ID: {pos.get('id')}")
            print(f"🧾 External ID: {pos.get('external_id')}")
            print(f"🏪 Store ID: {pos.get('store_id')}")
            print("-" * 40)
    else:
        print("⚠️ No se encontraron POS en tu cuenta.")
else:
    print("❌ Error al listar POS:", response.text)
