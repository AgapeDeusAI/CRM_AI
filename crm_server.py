from flask import Flask, request, jsonify
from flask_cors import CORS
from CRM_AI import CRM_AI

app = Flask(__name__)
CORS(app)

crm = CRM_AI()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "✅ CRM AI attivo"})

@app.route("/cliente", methods=["POST"])
def aggiungi_cliente():
    dati = request.get_json()
    nome = dati.get("nome")
    email = dati.get("email")
    if not nome or not email:
        return jsonify({"success": False, "errore": "Nome o email mancanti."})
    return jsonify(crm.aggiungi_cliente(nome, email))

@app.route("/interazione", methods=["POST"])
def interazione():
    dati = request.get_json()
    email = dati.get("email")
    messaggio = dati.get("messaggio")
    if not email or not messaggio:
        return jsonify({"success": False, "errore": "Dati mancanti."})
    return jsonify(crm.registra_interazione(email, messaggio))

@app.route("/scheda", methods=["GET"])
def scheda():
    email = request.args.get("email")
    if not email:
        return jsonify({"success": False, "errore": "Email mancante."})
    return jsonify({"success": True, "cliente": crm.scheda_cliente(email)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3017)