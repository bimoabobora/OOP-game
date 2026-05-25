from jogador import Jogador as player
from movimentoEcombate import Movimento
from inimigos import Inimigos
from estados import Mapa

class Interface:
    def atualizar(self, jogo):
        simbolo = input("Digite o simbolo do seu personagem: ")

        jogo.jogador = player(1,2,simbolo,10)
        jogo.mapa = Mapa.mapa2
        jogo.inimigo = Inimigos("@","Orc", 15, "Eu sou o orc bavo")
        jogo.estado = Movimento()



    





        
