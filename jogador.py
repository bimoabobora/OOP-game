from itens import Itens
item = Itens("Espada", "Espada super daora","Fisico", 5)
class Jogador():
    def __init__(self, linhaInicial: int, colunaInicial: int, simbolo: str, hp: int, inventario = item):
        self.linhaInicial = linhaInicial
        self.colunaInicial = colunaInicial
        self.simbolo = simbolo
        self.hp = hp
        self.inventario = [inventario]
    
    def pegar_itens(self):
        if self.inventario != None: 
         self.inventario.append(self.inventario)
        
    

    



    

        