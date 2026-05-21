from jogador import Jogador as player
from movimento import Movimento

class Interface:
    def atualizar(self, jogo):
        simbolo = input("Digite o simbolo do seu personagem: ")

        jogo.jogador = player(1,2,simbolo,10)

        jogo.estado = Movimento()



    





        
