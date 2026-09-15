class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'| {self._titulo} | {self._autor} | {self._ano_publicacao} | {self.disponivel}'

    def emprestar(self):
        self.disponivel = not self.disponivel
        return self.disponivel

    @property
    def disponibilidade(self):
        if self.disponivel:
            return f'| {self._titulo} | {self._autor} | {self._ano_publicacao} | Disponível'
        else:
            return f'| {self._titulo} | {self._autor} | {self._ano_publicacao} | Indisponível'

    @staticmethod
    def livros_publicados(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == str(ano)]
        return livros_disponiveis
