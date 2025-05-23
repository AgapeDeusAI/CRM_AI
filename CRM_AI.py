import json
import os
from datetime import datetime

class CRM_AI:
    def __init__(self, file_clienti="clienti.json"):
        self.file_clienti = file_clienti
        self.clienti = self._carica()

    def _carica(self):
        if os.path.exists(self.file_clienti):
            with open(self.file_clienti, "r") as f:
                return json.load(f)
        return {}

    def _salva(self):
        with open(self.file_clienti, "w") as f:
            json.dump(self.clienti, f, indent=2)

    def aggiungi_cliente(self, nome: str, email: str) -> dict:
        if email in self.clienti:
            return {"success": False, "errore": "Cliente già esistente."}
        self.clienti[email] = {
            "nome": nome,
            "email": email,
            "interazioni": []
        }
        self._salva()
        return {"success": True, "cliente": self.clienti[email]}

    def registra_interazione(self, email: str, messaggio: str) -> dict:
        if email not in self.clienti:
            return {"success": False, "errore": "Cliente non trovato."}
        interazione = {
            "data": datetime.now().isoformat(),
            "messaggio": messaggio
        }
        self.clienti[email]["interazioni"].append(interazione)
        self._salva()
        return {"success": True, "interazione": interazione}

    def scheda_cliente(self, email: str) -> dict:
        return self.clienti.get(email, {})