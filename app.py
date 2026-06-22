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
    for moeda in MOEDAS:
        for tentativa in range(3):
            try:
                url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
                resposta = requests.get(url, timeout=10)
                resposta.raise_for_status()
                dados = resposta.json()
                chave = f"{moeda}BRL"
                item = dados[chave]
                resultado[moeda] = {
                    "valor": float(item["bid"]),
                    "variacao": float(item["pctChange"]),
                    "alta": float(item["high"]),
                    "baixa": float(item["low"]),
                    "hora": item["create_date"]
                }
                break
            except Exception as e:
                if tentativa == 2:
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