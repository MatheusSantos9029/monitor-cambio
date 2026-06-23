from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

MOEDAS = ["USD", "EUR", "GBP", "JPY", "ARS"]

BANDEIRAS = {
    "USD": "us",
    "EUR": "eu",
    "GBP": "gb",
    "JPY": "jp",
    "ARS": "ar"
}

def buscar_cotacoes():
    resultado = {}
    try:
        url = "https://open.er-api.com/v6/latest/BRL"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        taxas = dados.get("rates", {})

        for moeda in MOEDAS:
            if moeda in taxas:
                valor = 1 / taxas[moeda]
                resultado[moeda] = {
                    "valor": valor,
                    "variacao": 0.0,
                    "alta": valor,
                    "baixa": valor,
                    "hora": dados.get("time_last_update_utc", "")
                }
            else:
                resultado[moeda] = {"erro": "Moeda não encontrada"}
    except Exception as e:
        for moeda in MOEDAS:
            resultado[moeda] = {"erro": str(e)}
    return resultado

@app.route("/")
def index():
    cotacoes = buscar_cotacoes()
    return render_template("index.html", cotacoes=cotacoes, bandeiras=BANDEIRAS)

@app.route("/api/cotacoes")
def api_cotacoes():
    return jsonify(buscar_cotacoes())

@app.route("/teste")
def teste():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url, timeout=10)
        return jsonify({"status": resposta.status_code, "dados": resposta.json()})
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run(debug=True)