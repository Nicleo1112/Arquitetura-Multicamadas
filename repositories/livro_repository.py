from models.livro_model import Livro

class LivroRepository:
    def __init__(self):
        self.livros = [
            Livro("Harry Potter e a Pedra Filosofal", "J.K Rowling", 1997),
            Livro("Harry Potter e a Câmara Secreta", "J.K Rowling", 1998),
            Livro("O Hobbit", "Tolkien", 1937),
            Livro("O Senhor dos Anéis", "Tolkien", 1954),
            Livro("Dom Casmurro", "Machado de Assis", 1899),
            Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881),
            Livro("Clean Code", "Robert C. Martin", 2008),
            Livro("Clean Architecture", "Robert C. Martin", 2017),
            Livro("Python Crash Course", "Eric Matthes", 2015),
            Livro("Automate the Boring Stuff", "Al Sweigart", 2015),
            Livro("The Pragmatic Programmer", "Andrew Hunt", 1999),
            Livro("Design Patterns", "Erich Gamma", 1994),
            Livro("Refactoring", "Martin Fowler", 1999),
            Livro("Código Limpo", "Robert C. Martin", 2009),
            Livro("Algoritmos", "Thomas H. Cormen", 2009),
            Livro("Estruturas de Dados", "Narasimha Karumanchi", 2011),
            Livro("Redes de Computadores", "Andrew S. Tanenbaum", 2010),
            Livro("Sistemas Operacionais", "Andrew S. Tanenbaum", 2015),
            Livro("Engenharia de Software", "Ian Sommerville", 2011),
            Livro("Introdução à Programação", "Deitel", 2012),
            Livro("Java: Como Programar", "Deitel", 2016),
            Livro("C Programming Language", "Kernighan", 1988),
            Livro("Artificial Intelligence", "Stuart Russell", 2010),
            Livro("Deep Learning", "Ian Goodfellow", 2016),
            Livro("Banco de Dados", "Elmasri", 2015),
            Livro("Compiladores", "Aho", 2006),
            Livro("Computer Organization", "Patterson", 2013),
            Livro("Digital Design", "Morris Mano", 2012),
            Livro("Data Science Handbook", "Jake VanderPlas", 2016),
            Livro("Fluent Python", "Luciano Ramalho", 2015),
        ]

    def listar_todos(self):
        return self.livros

    def adicionar(self, livro):
        self.livros.append(livro)