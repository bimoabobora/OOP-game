from movimento import Movimento

class Jogo:
    def __init__(self):
        self.estado = Movimento()

    def mudar_estado(self, novoEstado):
        self.estado = novoEstado
    
    def loop(self):
        while True:
            self.estado.atualizar(self)
            

game = Jogo()
game.loop()
