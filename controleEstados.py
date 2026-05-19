class Jogo:
    def __init__(self):
        self.estado = Movimento()

    def mudar_estado(self, novoEstado):
        self.estado = novoEstado
    
    def loop(self):
        while True:
            self.estado.atualizar(self)
            

class Movimento:
    def atualizar(self,jogo):
        print("ola")
        print("troca de estado")
        jogo.mudar_estado(Combate())
    
class Combate:
    def atualizar(self,jogo):
        print("trocou de estado")
        

game = Jogo()
game.loop()