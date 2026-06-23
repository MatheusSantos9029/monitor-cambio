from flask import Flask, render_template, jsonify
import requests
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///historico.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

MOEDAS = ["USD", "EUR", "GBP", "JPY", "ARS"]

BANDEIRAS = {
    "USD": "us",
    "EUR": "eu",
    "GBP": "gb",
    "JPY": "jp",
    "ARS": "ar"
}

class Cotacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hora = db.Column(db.String(20), nullable=False)
    moeda = db.Column(db.String(10), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

def buscar_cotacoes():
    resultado = {}
    try:
        url = "https://open.er-api.com/v6/latest/BRL"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        taxas = dados.get("rates", {})
        hora = datetime.now().strftime("%H:%M:%S")

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
                db.session.add(Cotacao(hora=hora, moeda=moeda, valor=valor))

        db.session.commit()

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

@app.route("/api/historico")
def api_historico():
    registros = Cotacao.query.order_by(Cotacao.criado_em.desc()).limit(100).all()

    agrupado = {}
    for r in registros:
        if r.hora not in agrupado:
            agrupado[r.hora] = {"hora": r.hora, "cotacoes": {}}
        agrupado[r.hora]["cotacoes"][r.moeda] = r.valor

    resultado = list(agrupado.values())[:20]
    resultado.reverse()

    return jsonify(resultado)

if __name__ == "__main__":
    app.run(debug=True)