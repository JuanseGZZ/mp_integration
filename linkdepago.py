import requests

import varibale 

ACCESS_TOKEN = varibale.TOKEN  

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

preference_data = {
    "items": [
        {
            "id": "prod001",
            "title": "Producto de prueba",
            "description": "Cobro vía link",
            "quantity": 1,
            "currency_id": "ARS",
            "unit_price": 1500.00
        }
    ],
    "external_reference": "pedido_001",  # Tu ID interno para relacionarlo luego
    "notification_url": "https://webhook.site/tu-url-de-webhook",  # Webhook para que te avise si pagaron
    "payer": {
        "name": "Cliente Test",
        "email": "cliente@example.com"
    },
    "back_urls": {
        "success": "https://tuweb.com/success",
        "failure": "https://tuweb.com/failure",
        "pending": "https://tuweb.com/pending"
    },
    "auto_return": "approved"
}

response = requests.post(
    "https://api.mercadopago.com/checkout/preferences",
    headers=headers,
    json=preference_data
)

if response.status_code != 201:
    print("❌ Error al crear el link de pago:", response.text)
else:
    init_point = response.json()["init_point"]
    print("✅ Link de pago generado:")
    print(init_point)
