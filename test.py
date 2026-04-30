from repositories.livro_repository import LivroRepository
from services.livro_service import LivroService

repo = LivroRepository()
service = LivroService(repo)

def teste_filtrar_por_nome():
    assert len(service.filtrar(titulo="Harry Potter")) == 2

def teste_filtrar_por_autor():
    assert len(service.filtrar(autor="J.K Rowling")) == 2

def teste_filtrar_por_ano():
    assert len(service.filtrar(ano_inicio=1970, ano_fim=2000)) == 2

def teste_adicionar_livro():
    total_antes = len(service.filtrar())
    service.adicionar("Novo Livro", "Autor Teste", 2023)
    assert len(service.filtrar()) == total_antes + 1

def teste_adicionar_livro_invalido():
    try:
        service.adicionar("", "", None)
        assert False, "Deveria ter lançado exceção"
    except ValueError:
        pass

if __name__ == "__main__":
    teste_filtrar_por_nome()
    teste_filtrar_por_autor()
    teste_filtrar_por_ano()
    teste_adicionar_livro()
    teste_adicionar_livro_invalido()
    print("Todos os testes passaram")