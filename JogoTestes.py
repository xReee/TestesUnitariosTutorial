from Jogo import Jogo
from Monstro import *
from Ataque import *
from Jogador import *
import unittest

class JogoTestes(unittest.TestCase):
    def setUp(self):
        self.monstro = MonstroDummy()
        self.jogador = JogadorDummy()
        self.sut = Jogo(self.monstro, self.jogador)
    
    def tearDown(self):
        del self.sut
        del self.monstro
        del self.jogador
    
    def teste_atacar_givenMonstroSemDefasa_whenAtacar_thenMonstroGerouDefesa(self):
        #given
        self.monstro = MonstroSpy()
        self.sut = Jogo(self.monstro, self.jogador)
        self.monstro.defesa = []

        #when
        self.sut.atacar(AtaqueDummy([]))

        #then
        self.assertEqual(self.monstro.gerarDefesaCount, 1)

    def teste_atacar_givenRespostaQuaseCorreta_whenAtacar_thenDeveTerRespostasCorretas_andRespostasQuaseCorretas(self):
        #given
        self.monstro = MonstroStub() # ataque do monstro = [1, 5, 2, 4]
        self.sut = Jogo(self.monstro, self.jogador)
        ataque = Ataque([1, 2, 5, 4])

        #when
        self.sut.atacar(ataque)

        #then
        self.assertEqual(ataque.armasCorretasNaPosicaoCorreta, 2)
        self.assertEqual(ataque.armasCorretasNaPosicaoErrada, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
