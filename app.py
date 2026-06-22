from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

MOEDAS = ["USD", "EUR"]

def buscar_cotacoes():
    resultado = {}
    for moeda in MOEDAS:
        try:
            url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
            resposta = requests.get(url, timeout=5)
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
        except Exception as e:
            resultado[moeda] = {"erro": str(e)}
    return resultado

@app.route("/")
def index():
    cotacoes = buscar_cotacoes()
    return render_template("index.html", cotacoes=cotacoes)

@app.route("/api/cotacoes")
def api_cotacoes():
    return jsonify(buscar_cotacoes())

if __name__ == "__main__":
    app.run(debug=True)