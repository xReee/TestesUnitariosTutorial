import unittest

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

        return self.conferirSeGanhou()

    def acertouAtaque(self):
        self.armasCorretasNaPosicaoCorreta += 1

    def acertouArma(self):
        self.armasCorretasNaPosicaoErrada += 1

    def conferirSeGanhou(self):
        return self.armasCorretasNaPosicaoCorreta == 5

class AtaqueTests(unittest.TestCase):
    def teste_conferirAtaque_quandoTiverArmaCertaPosErrada(self):
        armas = [1,2,3,4]
        ataque = Ataque(armas)
        defesaDoMonstro = [1,2,4,3] # tem 2 armas certas e duas armas erradas, ne?

        ataque.conferirAtaque(defesaDoMonstro)

        self.assertEqual(ataque.armasCorretasNaPosicaoCorreta, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoErrada, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)