# Livraria — Arquitetura Multicamada
# NOVA FEATURE ----> Adicionar novos livros a lista

Aplicação web para busca e cadastro de livros, desenvolvida em Python com Flask, seguindo uma arquitetura multicamada com 4 camadas bem definidas.

Arquitetura

O projeto segue uma Arquitetura Multicamada, onde cada camada tem uma responsabilidade única e se comunica apenas com a camada adjacente.

controllers/     → Camada 1: recebe requisições HTTP e retorna respostas
services/        → Camada 2: contém as regras de negócio
repositories/    → Camada 3: acesso e manipulação dos dados
models/          → Camada 4: define a estrutura dos dados

templates/       → View: interface HTML renderizada pelo Flask
Fluxo de uma requisição
Usuário → Controller → Service → Repository → Model
                                               ↓



Funcionalidades
Filtrar livros por título, autor e intervalo de ano
Adicionar novos livros à lista
Validação de dados na camada de serviço
Testes unitários com test.py
Testes BDD com Behave
Como executar
Pré-requisitos
Python 3.8+
pip
Instalação
# Clone o repositório
git clone https://github.com/seu-usuario/Arquitetura-MVC.git
cd Arquitetura-MVC

# Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/Mac

# Instale as dependências
pip install flask behave
Rodando a aplicação
python app.py

Acesse em: http://127.0.0.1:5000

Testes
Testes unitários
python test.py
Testes BDD (Behave)
behave
Descrição das Camadas
Camada 1 — Controller (controllers/livro_controller.py)

Recebe as requisições HTTP, extrai os parâmetros e delega para o Service. Não contém regras de negócio.

Camada 2 — Service (services/livro_service.py)

Contém as regras de negócio, como validação de campos obrigatórios e intervalo de ano válido. Orquestra as operações entre Controller e Repository.

Camada 3 — Repository (repositories/livro_repository.py)

Responsável pelo acesso aos dados. Armazena a lista de livros em memória e oferece métodos para listar e adicionar.

Camada 4 — Model (models/livro_model.py)

Define a estrutura do objeto Livro com seus atributos (titulo, autor, ano) e o método to_dict() para serialização.

Tecnologias
Tecnologia	Uso
Python	Linguagem principal
Flask	Framework web
Behave	Testes BDD
Bootstrap 5	Estilização da interface
