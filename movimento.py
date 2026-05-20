import time
import keyboard
from jogador import Jogador as player
from mapa import Mapa as map
from combate import Combate

class Movimento:

    def atualizar(self,jogo):
        tecla = keyboard.read_key()
        self.movimento(player, tecla, map.mapa2)



    def movimento(player,move, matriz):
        linha = player.linhaInicial
        coluna = player.colunaInicial
        simbolo = player.simbolo

        match move: 
            case "w":
                try:
                 matriz[linha][coluna] = '.'
                 linha -= 1
                 
                 matriz[linha][coluna] = simbolo
                 player.linhaInicial = linha
                except IndexError:
                    linha += 1
                    matriz[linha][coluna] = simbolo
            case "s":
                try:
                    matriz[linha][coluna] = '.'
                    linha += 1
                    
                    matriz[linha][coluna] = simbolo
                    player.linhaInicial = linha
                except IndexError:
                    linha -= 1
                    matriz[linha][coluna] = simbolo
            case "a":
                try:
                    matriz[linha][coluna] = '.'
                    coluna -= 1
                    
                    matriz[linha][coluna] = simbolo
                    player.colunaInicial = coluna
                except IndexError:
                    coluna += 1
                    matriz[linha][coluna] = simbolo
            case "d":
                try:
                 matriz[linha][coluna] = '.'
                 coluna += 1
                 
                 matriz[linha][coluna] = simbolo
                 player.colunaInicial = coluna
                except IndexError:
                    coluna -= 1
                    matriz[linha][coluna] = simbolo
        map.printmapa(map.mapa2)
        time.sleep(0.2)
    
    def detectar_inimigo(matriz,linha,coluna):
        if matriz[linha][coluna] != ".":
            return True
        return False
    
    
    

