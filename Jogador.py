class Jogador:
    def __init__(self, vidasDoJogador):
        self.vidasDoJogador = vidasDoJogador
    
    def __del__(self):
        self.vidasDoJogador = 0

    def foiDerrotado(self):
        return self.vidasDoJogador == 0

    def sofrerDano(self):
        self.vidasDoJogador -= 1

class JogadorDummy(Jogador):
    def __init__(self):
        self.vidasDoJogador = 3

    def __del__(self):
        self.vidasDoJogador = 0
