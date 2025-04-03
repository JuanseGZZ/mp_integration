from flask import Flask, request
import sqlite3, requests

import varibale  

app = Flask(__name__)
ACCESS_TOKEN = varibale.TOKEN

# Función para consultar el estado del pago
def obtener_pago(payment_id):
    response = requests.get(
        f"https://api.mercadopago.com/v1/payments/{payment_id}",
        headers={"Authorization": f"Bearer {ACCESS_TOKEN}"}
    )
    return response.json()

# Webhook
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data.get("type") == "payment":
        payment_id = data["data"]["id"]
        pago = obtener_pago(payment_id)

        if pago["status"] == "approved":
            external_ref = pago["external_reference"]

            # Actualizás en la base de datos
            conn = sqlite3.connect("pagos.db")
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE pagos SET estado = 'aprobado' WHERE external_reference = ? AND estado = 'pendiente'",
                (external_ref,)
            )
            conn.commit()
            conn.close()

            print(f"✅ Pago aprobado para referencia {external_ref}")

    return "OK", 200
