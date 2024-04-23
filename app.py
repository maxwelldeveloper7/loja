from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja_online.db'
db = SQLAlchemy(app)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade_estoque = db.Column(db.Integer, nullable=False, default=0)

with app.app_context():
    db.create_all()

@app.route('/adicionar_produto', methods=['GET', 'POST'])
def adicionar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = float(request.form['preco'])
        quantidade_estoque = int(request.form['quantidade_estoque'])
        novo_produto = Produto(nome=nome, preco=preco, quantidade_estoque=quantidade_estoque)
        db.create_all()
        db.session.add(novo_produto)
        db.session.commit()
        return redirect(url_for('listar_produtos'))
    return render_template('adicionar_produto.html')

@app.route('/listar_produtos')
def listar_produtos():
    db.create_all()
    produtos = Produto.query.all()    
    return render_template('listar_produtos.html', produtos=produtos)


# Nova rota para editar produto
@app.route('/editar_produto/<int:id>', methods=['GET', 'POST'])
def editar_produto(id):
    produto = Produto.query.get_or_404(id)  # Encontra o produto ou retorna 404 se não existir

    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.preco = float(request.form['preco'])
        produto.quantidade_estoque = int(request.form['quantidade_estoque'])

        db.session.commit()  # Atualiza o produto no banco de dados
        return redirect(url_for('listar_produtos'))  # Retorna para a lista de produtos

    # Renderiza um formulário para editar o produto com valores atuais
    return render_template('editar_produto.html', produto=produto)


@app.route('/excluir_produto/<int:id>', methods=['POST', 'GET'])
def excluir_produto(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('listar_produtos'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)