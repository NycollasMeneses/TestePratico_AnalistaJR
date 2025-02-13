from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint GET /saudacao
@app.route('/saudacao', methods=['GET']) # /saudacao?nome=
def saudacao():
    nome = request.args.get('nome', 'Mundo')  # Se nenhum nome for passado, usa "Mundo"
    return jsonify({"mensagem": f"Olá, {nome}!"})

# Endpoint POST /soma
@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    
    if not dados or 'num1' not in dados or 'num2' not in dados:
        return jsonify({"erro": "Os campos 'num1' e 'num2' são obrigatórios"}), 400
    
    try:
        num1 = float(dados['num1']) # {Passe os parametros "num1": 10, "num2": 5.5}
        num2 = float(dados['num2'])
        resultado = num1 + num2
        return jsonify({"soma": resultado})
    except ValueError:
        return jsonify({"erro": "Os valores devem ser numéricos"}), 400

# Executa a API
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
