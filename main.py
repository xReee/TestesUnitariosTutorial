from Monstro import Monstro
from Ataque import Ataque
from Jogador import Jogador
from Jogo import Jogo

def retornarNomeDaArma(arma):
    nomeArma = ""
    if arma == 0:
        nomeArma = "Espada"
    elif arma == 1:
        nomeArma = "Arco e flecha"
    elif arma == 2:
        nomeArma = "Machado"
    elif arma == 3:
        nomeArma = "Lanca"
    elif arma == 4:
        nomeArma = "Faca"
    elif arma == 5:
        nomeArma = "Besta"

    return nomeArma

def retornarArmasNomes(array):
    armasNome  = []
    for arma in array:
        armasNome.append(retornarNomeDaArma(arma))
    
    return armasNome

monstro = Monstro()
monstro.gerarDefesa()
jogador = Jogador(5)
jogo = Jogo(monstro, jogador)
print("-------------------------------------------------")

while(jogo.vitoria == False):
    print("Vamos jogar? Voce precisa escolher 4 armas, precisa ser igual as armas do monstro e precisam estar na posicao correta e tambem nao podem ser iguais, aqui as opcoes:")
    print("1.Espada\n2.Arco e flecha\n3.Machado\n4.Lanca\n5.Faca\n6.Besta\n")
    armasJogador = []
    i = 0
    while(i < 4):
        i += 1
        resposta = input() - 1
        armasJogador.append(resposta)
        print("Voce adicionou \"" + str(retornarNomeDaArma(resposta)) + "\" na lista de ataques")
    ataque = Ataque(armasJogador)


    jogo.atacar(ataque)
    print("\n**** RESULTADO DO ATAQUE ****")
    print("Seu ataque:" + str(retornarArmasNomes(armasJogador))) 

    # - Debug only:
    # print(retornarArmasNomes(monstro.defesa))

    print("Acertou " + str(ataque.armasCorretasNaPosicaoCorreta) + " armas corretas e na posicao correta")
    print("Acertou " + str(ataque.armasCorretasNaPosicaoErrada) + " armas corretas mas na posicao errada")
    

    if jogo.vitoria:  
        print("parabens ganhou")
    else:
        print("Errou, tente de novo!")

    print("****************************\n")

   
