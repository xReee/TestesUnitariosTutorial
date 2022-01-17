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

