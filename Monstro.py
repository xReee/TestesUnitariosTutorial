import random

class Monstro:
    def __init__(self):
        self.defesa = []
    
    def __del__(self):
        self.defesa = []

    def gerarDefesa(self):
        data = range(0, 6)
        random.shuffle(data)
        self.defesa = data[:4]

class MonstroDummy(Monstro):
    pass

class MonstroSpy(Monstro):
    def __init__(self):
        self.defesa = []
        self.gerarDefesaCount = 0
    
    def __del__(self):
        self.defesa = []
        self.gerarDefesaCount = 0

    def gerarDefesa(self):
        self.gerarDefesaCount += 1

class MonstroStub(Monstro):
    def gerarDefesa(self):
        self.defesa = [1, 5, 2, 4]
