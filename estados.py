from interface import Interface
from inimigos import Inimigos
from itens import Itens


class Jogo:
    def __init__(self):
        self.inimigo = Inimigos("#","Dragão Zika das Ideias",10,"EU SER BAVO")
        self.item = Itens("Espada", "Espada super daora","Fisico",5)
        Mapa.gerarInimigos(Mapa.mapa1,self.inimigo)
        Mapa.gerarItens(Mapa.mapa1,self.item)
        self.jogador = None
        self.mapa = Mapa.mapa1
        self.estado = Interface()

    
    def loop(self):
        while True:
            self.estado.atualizar(self)
     
            
class Mapa:
    mapa1 = [['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],]
    
    mapa2 = [['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],]
    
    def gerarInimigos(matriz,jogo):
        matriz[0][1] = jogo.simbolo

    def gerarItens(matriz,jogo):
        matriz[2][0] = jogo.simbolo
    
    def printmapa(matriz):
        for row in matriz:
            print(row)            



