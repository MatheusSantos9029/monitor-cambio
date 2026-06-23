# 💱 Monitor de Câmbio

> *"São pequenos passos que nos fazem trilhar grandes caminhos."*

🌐 **Acesse o projeto:** [monitor-cambio.onrender.com](https://monitor-cambio.onrender.com)

---

## 🇧🇷 Português

### Sobre o projeto

Aplicação web desenvolvida com Flask que monitora cotações de moedas estrangeiras em relação ao Real (BRL) em tempo real. O projeto consome a ExchangeRate-API, exibe gráficos de flutuação, permite conversão de valores, dispara alertas visuais e salva o histórico em banco de dados SQLite.

Desenvolvido como parte do meu aprendizado prático em Python e desenvolvimento web, explorando Flask, APIs, banco de dados e deploy em produção.

### Funcionalidades

- 📊 Cotações em tempo real de USD, EUR, GBP, JPY e ARS
- 🏳️ Bandeiras dos países em cada card de moeda
- ⏱️ Atualização automática configurável (30s, 1min ou 5min)
- 💱 Conversor de BRL para qualquer moeda listada
- ⚠️ Alerta visual (card pisca) quando a cotação ultrapassa ou cai abaixo de um valor definido
- 📋 Histórico dos últimos 20 registros ao lado do gráfico
- 📈 Gráfico de flutuação em tempo real (USD e EUR)
- 💾 Histórico salvo em banco de dados SQLite

### Tecnologias utilizadas

- Python 3.12
- [Flask](https://flask.palletsprojects.com/) — framework web
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) — ORM para banco de dados
- [SQLite](https://www.sqlite.org/) — banco de dados local
- [ExchangeRate-API](https://www.exchangerate-api.com/) — cotações em tempo real
- [Chart.js](https://www.chartjs.org/) — gráficos interativos
- [Flag Icons CSS](https://flagicons.lipis.dev/) — bandeiras dos países
- [Gunicorn](https://gunicorn.org/) — servidor WSGI para produção
- [Render](https://render.com/) — hospedagem gratuita

### Pré-requisitos

- Python 3.10 ou superior

### Como usar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/MatheusSantos9029/monitor-cambio.git
cd monitor-cambio
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Execute o servidor**
```bash
python app.py
```

**4. Acesse no navegador**
```
http://localhost:5000
```

### Estrutura do projeto

```
monitor-cambio/
│
├── app.py                  # Servidor Flask e lógica da aplicação
├── requirements.txt        # Dependências do projeto
├── Procfile                # Configuração para deploy no Render
├── .gitignore              # Arquivos ignorados pelo Git
├── templates/
│   └── index.html          # Interface web
├── static/
│   └── style.css           # Estilo da aplicação
└── instance/
    └── historico.db        # Banco de dados SQLite (gerado automaticamente)
```

---

## 🇺🇸 English

### About

A Flask web application that monitors foreign currency exchange rates against the Brazilian Real (BRL) in real time. The project consumes the ExchangeRate-API, displays fluctuation charts, allows value conversion, triggers visual alerts, and saves history to a SQLite database.

Built as part of my hands-on learning journey in Python and web development, exploring Flask, APIs, databases, and production deployment.

### Features

- 📊 Real-time exchange rates for USD, EUR, GBP, JPY, and ARS
- 🏳️ Country flags on each currency card
- ⏱️ Configurable auto-refresh (30s, 1min, or 5min)
- 💱 BRL converter to any listed currency
- ⚠️ Visual alert (card blinks) when rate exceeds or drops below a set value
- 📋 Last 20 records displayed beside the chart
- 📈 Real-time fluctuation chart (USD and EUR)
- 💾 History saved to SQLite database

### Technologies

- Python 3.12
- [Flask](https://flask.palletsprojects.com/) — web framework
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) — database ORM
- [SQLite](https://www.sqlite.org/) — local database
- [ExchangeRate-API](https://www.exchangerate-api.com/) — real-time exchange rates
- [Chart.js](https://www.chartjs.org/) — interactive charts
- [Flag Icons CSS](https://flagicons.lipis.dev/) — country flags
- [Gunicorn](https://gunicorn.org/) — WSGI server for production
- [Render](https://render.com/) — free hosting

### Requirements

- Python 3.10 or higher

### How to run locally

**1. Clone the repository**
```bash
git clone https://github.com/MatheusSantos9029/monitor-cambio.git
cd monitor-cambio
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the server**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

### Project structure

```
monitor-cambio/
│
├── app.py                  # Flask server and application logic
├── requirements.txt        # Project dependencies
├── Procfile                # Render deployment config
├── .gitignore              # Git ignored files
├── templates/
│   └── index.html          # Web interface
├── static/
│   └── style.css           # Application styles
└── instance/
    └── historico.db        # SQLite database (auto-generated)
```

---

*Developed by [Matheus Santos](https://github.com/MatheusSantos9029)*
