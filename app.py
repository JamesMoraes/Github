from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuração da conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="novousuario",
    passwd="usuario123",
    db="exemplo"
)

# Função para formatar número com duas casas decimais e substituir ponto por vírgula
def formatar_numero(numero):
    return f"{numero:.2f}".replace('.', ',')

# Função para converter data no formato dia/mês/ano para ano-mês-dia
def formatar_data(data):
    return datetime.strptime(data, '%d/%m/%Y').strftime('%Y-%m-%d')

# Função para formatar data no formato ano-mês-dia para dia/mês/ano
def formatar_data_inversa(data):
    return data.strftime('%d/%m/%Y')

@app.route('/')
def index():
    return redirect('/produtos')

@app.route('/produtos')
def produtos():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    produtos_formatados = [
        # Forma de listagem de dados
        # com compressão de lista
        {
            'id': produto[0],
            'nome': produto[1],
            'preco': formatar_numero(produto[2]),
            'fabricacao': formatar_data_inversa(produto[3])
        }
        for produto in produtos

    ]

    # Forma alternativa
    # Usando map (mapeamento de propriedades)
    # e a função nativa 'lambda'

    """ 
    produtos_formatados = list(map(lambda produto: {
            'id': produto[0],
            'nome': produto[1],
            'preco': formatar_numero(produto[2]),
            'fabricacao': formatar_data_inversa(produto[3])
    }, produtos))
    
    """

    return render_template('produtos.html', produtos=produtos_formatados)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco'].replace(',', '.')
        fabricacao = formatar_data(request.form['fabricacao'])

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, preco, fabricacao) VALUES (%s, %s, %s)",
            (nome, preco, fabricacao)
        )
        db.commit()
        return redirect('/produtos')
    
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)