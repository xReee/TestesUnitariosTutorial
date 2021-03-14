from Monstro import Monstro
from Ataque import Ataque
import unittest

class Jogo:
    def __init__(self, monstro, jogador):
        self.monstro = monstro
        self.vitoria = False
        self.jogador = jogador
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0

    def __del__(self):
        del self.monstro
        self.vitoria = False

    def atacar(self, ataque):
        if self.monstro.defesa == []:
            self.monstro.gerarDefesa()
           
        self.vitoria = ataque.conferirAtaque(self.monstro.defesa)

        if not self.vitoria:
            self.jogador.perderVida()
