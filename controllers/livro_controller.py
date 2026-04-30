from flask import Blueprint, render_template, request, redirect, url_for
from repositories.livro_repository import LivroRepository
from services.livro_service import LivroService

livro_bp = Blueprint('livro', __name__)
repository = LivroRepository()
service = LivroService(repository)

@livro_bp.route('/', methods=['GET'])
def index():
    titulo = request.args.get('titulo', '')
    autor = request.args.get('autor', '')
    try:
        ano_min = int(request.args.get('ano_min'))
        ano_max = int(request.args.get('ano_max'))
    except (TypeError, ValueError):
        ano_min, ano_max = None, None

    livros = service.filtrar(titulo, autor, ano_min, ano_max)
    return render_template('index.html', livros=[l.to_dict() for l in livros])

@livro_bp.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form.get('titulo', '')
    autor = request.form.get('autor', '')
    try:
        ano = int(request.form.get('ano'))
    except (TypeError, ValueError):
        ano = None
    try:
        service.adicionar(titulo, autor, ano)
    except ValueError:
        pass
    return redirect(url_for('livro.index'))