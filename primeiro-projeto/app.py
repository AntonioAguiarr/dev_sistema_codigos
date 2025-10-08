from flask import Flask
# importando a classe flask do modulo flask

# criar uma instancia do flask = objeto
app = Flask(__name__)
# __name__ é o nome do modulo atual -> navegação


# quando acessar ao servidor, chame essa função
@app.route('/')
def hello_world():
    return 'hello, world'
# flask ele converte string em um resposta http
# executa o servidor
if __name__ == '__main__':
    app.run(debug=True)

