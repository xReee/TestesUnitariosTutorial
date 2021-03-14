class Ataque:
    def __init__(self, armas):
        self.armas = armas
        self.armasCorretasNaPosicaoCorreta = 0
        self.armasCorretasNaPosicaoErrada = 0

    def __del__(self):
        self.armas = []

    def conferirAtaque(self, defesaDoMonstro):
        count = 0

        for armaDefensiva in defesaDoMonstro:
            if armaDefensiva == self.armas[count]:
                self.acertouAtaque()

            elif armaDefensiva in self.armas:
                self.acertouArma()

            count += 1

        return self.conferirSeGanhou

    def acertouAtaque(self):
        self.armasCorretasNaPosicaoCorreta += 1

    def acertouArma(self):
        self.armasCorretasNaPosicaoErrada += 1

    def conferirSeGanhou(self):
        return self.armasCorretasNaPosicaoCorreta == 4


class AtaqueDummy(Ataque):
    pass
