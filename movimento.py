import time
import keyboard
from jogador import Jogador as player
from mapa import Mapa as map
from combate import Combate

class Jogo:
    def __init__(self):
        self.estado = Movimento()
    
    def loop(self):
        while True:
         self.estado.atualizar(self)


class Movimento:
    tecla = keyboard.read_key()
    @staticmethod
    def movimento(jogo,player,move = tecla, matriz = []):
        linha = player.linhaInicial
        coluna = player.colunaInicial
        simbolo = player.simbolo

        match move: 
            case "w":
                try:
                 matriz[linha][coluna] = '.'
                 linha -= 1
                 Movimento.atualizar(jogo,matriz,linha,coluna)
                 matriz[linha][coluna] = simbolo
                 player.linhaInicial = linha
                except IndexError:
                    linha += 1
                    matriz[linha][coluna] = simbolo
            case "s":
                try:
                    matriz[linha][coluna] = '.'
                    linha += 1
                    Movimento.atualizar(jogo,matriz,linha,coluna)
                    matriz[linha][coluna] = simbolo
                    player.linhaInicial = linha
                except IndexError:
                    linha -= 1
                    matriz[linha][coluna] = simbolo
            case "a":
                try:
                    matriz[linha][coluna] = '.'
                    coluna -= 1
                    Movimento.atualizar(jogo,matriz,linha,coluna)
                    matriz[linha][coluna] = simbolo
                    player.colunaInicial = coluna
                except IndexError:
                    coluna += 1
                    matriz[linha][coluna] = simbolo
            case "d":
                try:
                 matriz[linha][coluna] = '.'
                 coluna += 1
                 Movimento.atualizar(jogo,matriz,linha,coluna)
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
    
    def atualizar(jogo,matriz, linha,coluna):
      if Movimento.detectar_inimigo(matriz,linha,coluna):
          jogo.estado = Combate().printinfo(1)
            
jogo = Jogo()
jogador = player(2,1,"#",5)

#Movimento.movimento(jogo,jogador,map.mapa2)
Jogo().loop()
    
    

