from flask import Flask, render_template
import os

app = Flask(__name__)

def leer_nueva_respuesta():
    with open("data/texto_generado.txt",'r') as f:
        respuesta = f.read()
    return respuesta

@app.route("/")
def home():
    generated_text = leer_nueva_respuesta()
    return render_template('index.html',generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)



