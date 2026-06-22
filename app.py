from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

MOEDAS = ["USD", "EUR", "BTC", "GBP", "JPY", "ARS"]

BANDEIRAS = {
    "USD": "us",
    "EUR": "eu",
    "BTC": "btc",
    "GBP": "gb",
    "JPY": "jp",
    "ARS": "ar"
}

def buscar_cotacoes():
    resultado = {}
    try:
        pares = ",".join([f"{moeda}-BRL" for moeda in MOEDAS])
        url = f"https://economia.awesomeapi.com.br/json/last/{pares}"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        for moeda in MOEDAS:
            chave = f"{moeda}BRL"
            if chave in dados:
                item = dados[chave]
                resultado[moeda] = {
                    "valor": float(item["bid"]),
                    "variacao": float(item["pctChange"]),
                    "alta": float(item["high"]),
                    "baixa": float(item["low"]),
                    "hora": item["create_date"]
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