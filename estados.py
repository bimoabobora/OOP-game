from interface import Interface
class Jogo:
    def __init__(self):
        self.inimigo = None
        self.jogador = None
        self.estado = Interface()

    
    def loop(self):
        while True:
            self.estado.atualizar(self)
            
            

game = Jogo()
game.loop()
