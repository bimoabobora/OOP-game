import time
import keyboard
from mapa import Mapa as map
from combate import Combate
from inimigos import Inimigos

class Movimento:

    def atualizar(self,jogo):
        tecla = keyboard.read_key()
        if self.movimento(jogo.jogador, tecla, map.mapa2) == True:
            jogo.inimigo = Inimigos("Orc", 15)
            jogo.estado = Combate()



    def movimento(self,player,move, matriz):
        linha = player.linhaInicial
        coluna = player.colunaInicial
        simbolo = player.simbolo

        match move: 
            case "w":
                try:
                 matriz[linha][coluna] = '.'
                 linha -= 1
                 
                 if self.detectar_inimigo(map.mapa2,linha,coluna):
                     return True
                 
                 matriz[linha][coluna] = simbolo
                 player.linhaInicial = linha
                except IndexError:
                    linha += 1
                    matriz[linha][coluna] = simbolo
            case "s":
                try:
                    matriz[linha][coluna] = '.'
                    linha += 1
                    if self.detectar_inimigo(map.mapa2,linha,coluna):
                        return True
                    matriz[linha][coluna] = simbolo
                    player.linhaInicial = linha
                except IndexError:
                    linha -= 1
                    matriz[linha][coluna] = simbolo
            case "a":
                try:
                    matriz[linha][coluna] = '.'
                    coluna -= 1
                    if self.detectar_inimigo(map.mapa2,linha,coluna):
                        return True
                    matriz[linha][coluna] = simbolo
                    player.colunaInicial = coluna
                except IndexError:
                    coluna += 1
                    matriz[linha][coluna] = simbolo
            case "d":
                try:
                 matriz[linha][coluna] = '.'
                 coluna += 1
                 if self.detectar_inimigo(map.mapa2,linha,coluna):
                     return True
                 matriz[linha][coluna] = simbolo
                 player.colunaInicial = coluna
                except IndexError:
                    coluna -= 1
                    matriz[linha][coluna] = simbolo
        map.printmapa(map.mapa2)
        time.sleep(0.2)
    
    def detectar_inimigo(self,matriz,linha,coluna):
        if matriz[linha][coluna] != ".":
            return True
        return False
    
    
    

