from interface import Interface
class Jogo:
    def __init__(self):
        self.inimigo = None
        self.jogador = None
        self.mapa = Mapa.map1
        self.estado = Interface()

    
    def loop(self):
        while True:
            self.estado.atualizar(self)
     
            
class Mapa(Jogo):
    mapa1 = [['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],]
    
    mapa2 = [['.',Jogo.inimigo.simbolo,'.'],
             ['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],
             ['.','.','.'],]
    
    def printmapa(matriz):
        for row in matriz:
            print(row)            

game = Jogo()
game.loop()

