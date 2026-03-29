from flask import Flask, request, render_template_string
import subprocess
import os

app = Flask(__name__)

# -----------------------------------------------------------------
# AVISO: Este código contém vulnerabilidades INTENCIONAIS
# para fins educacionais de DevSecOps.
# NÃO use em produção!
# -----------------------------------------------------------------

SECRET_KEY = "super_secret_123"  # nosec - vulnerabilidade intencional (hardcoded secret)

@app.route("/")
def home():
    return """
    <h1>🔒 DevSecOps Demo App</h1>
    <p>Endpoints disponíveis:</p>
    <ul>
        <li><a href="/login?user=joao">/login?user=joao</a> — Login (XSS vulnerável)</li>
        <li><a href="/ping?host=8.8.8.8">/ping?host=8.8.8.8</a> — Ping (Command Injection vulnerável)</li>
        <li><a href="/health">/health</a> — Health check</li>
    </ul>
    """

@app.route("/login")
def login():
    user = request.args.get("user", "")
    # VULNERABILIDADE: XSS — user input renderizado sem sanitização
    return render_template_string(f"<h2>Bem vindo {user}!</h2>")  # nosec

@app.route("/ping")
def ping():
    host = request.args.get("host", "8.8.8.8")
    # VULNERABILIDADE: Command Injection — input direto no shell
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)  # nosec
    return f"<pre>{output.decode()}</pre>"

@app.route("/health")
def health():
    return {"status": "ok", "version": "1.0.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # nosec - debug mode intencional
