import requests
import qrcode

import varibale

ACCESS_TOKEN = varibale.TOKEN
USER_ID = varibale.USER_ID  # Ej: 123456789
POS_EXTERNAL_ID = varibale.POS_EXTERNAL_ID  # El external_id del POS que ya tenés creado

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Crear la orden QR
payload = {
    "external_reference": "pedido_123_cliente_juan",
    "title": "Servicio técnico",
    "description": "Servicio completo para notebook",  # <--- este es el que faltaba
    "notification_url": "https://webhook.site/tu-url",
    "total_amount": 5000,
    "items": [
        {
            "sku_number": "ST001",
            "category": "others",
            "title": "Reparación notebook",
            "description": "Servicio completo",
            "unit_price": 5000,
            "quantity": 1,
            "unit_measure": "unit",
            "total_amount": 5000
        }
    ]
}


url = f"https://api.mercadopago.com/instore/orders/qr/seller/collectors/{USER_ID}/pos/{POS_EXTERNAL_ID}/qrs"

response = requests.put(url, headers=headers, json=payload)

if response.status_code == 200:
    qr_data = response.json()["qr_data"]
    print("QR Data:", qr_data)
    qr_img = qrcode.make(qr_data)
    qr_img.save("qr_dinamico_nuevo.png")
    print("✅ QR generado con éxito. Guardado como 'qr_dinamico_nuevo.png'")
else:
    print("❌ Error al generar QR:", response.status_code, response.text)
