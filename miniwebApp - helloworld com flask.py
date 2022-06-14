# Criando minha primeira aplicação web
from flask import Flask

# Definindo o app
app = Flask(__name__)

# Definindo o diretório raiz
@app.route("/")

# Criando a função
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()