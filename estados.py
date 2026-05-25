from interface import Interface
from inimigos import Inimigos

class Jogo:
    def __init__(self):
        self.inimigo = Inimigos("#","Dragão Zika das Ideias",10,"EU SER BAVO")
        Mapa.gerarInimigos(Mapa.mapa1,self.inimigo)
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
    
    def printmapa(matriz):
        for row in matriz:
            print(row)            



