from flask import Flask, request

app = Flask(__name__)

captured_code = None

@app.route("/callback")
def callback():
    global captured_code
    code = request.args.get("code", "AUCUN CODE")
    captured_code = code
    return f"""
    <h1>✅ Code capturé !</h1>
    <p>Copie ce code dans ton terminal Python :</p>
    <pre style="background:#f4f4f4;padding:15px;font-size:18px;">{code}</pre>
    """

@app.route("/")
def home():
    global captured_code
    if captured_code:
        return f"Code en attente : <pre>{captured_code}</pre>"
    return "En attente de callback..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(__import__("os").environ.get("PORT", 8000)))   