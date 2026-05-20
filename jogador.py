
class Jogador():
    def __init__(self, linhaInicial: int, colunaInicial: int, simbolo: str, hp: int, inventario = None):
        self.linhaInicial = linhaInicial
        self.colunaInicial = colunaInicial
        self.simbolo = simbolo
        self.hp = hp
        self.inventario = inventario
    
    def pegar_itens(self):
        if self.itens != None: 
         itensJogador= []
         itensJogador.append(self.itens)
         return itensJogador
    

    



    

        