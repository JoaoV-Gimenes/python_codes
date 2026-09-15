from modules import avaliacao
from modules.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, comida):
        self._nome = nome.title()
        self._comida = comida.upper()
        self._aberto = False
        self._avaliacaoRes = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Restaurente: {self._nome} , Tipo de comida: {self._comida}'

    @property
    def estado_restaurante(self):
        return "0" if self._aberto else "X"

    def alternar_estado(self):
        self._aberto = not self._aberto
        return self._aberto

    @classmethod
    def listar_elementos(cls):
        print(f'{'Nome do restaurante'.ljust(15)} |{'Categoria'.ljust(20)}|{'Avaliação'.ljust(20)}|{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)}|{restaurante._comida.ljust(20)}|{str(restaurante.media_avaliacoes).ljust(20)}|{restaurante.estado_restaurante.ljust(20)}')

    def receber_avaliacao(self, nome, nota):
        if 0 < nota <= 5:
            avaliacaoF = Avaliacao(nome, nota)
            self._avaliacaoRes.append(avaliacaoF)

    @property
    def media_avaliacoes(self):
        if not self._avaliacaoRes:
            return 'NA'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacaoRes)
        notaF = round(soma_notas/len(self._avaliacaoRes), 1)
        return notaF

