import time
import keyboard


class Movimento:

    def atualizar(self,jogo):
        #tecla = keyboard.read_key()
        tecla = input("")
        if self.movimento(jogo.jogador, tecla, jogo.mapa) == True:
            jogo.estado = Combate()



    def movimento(self,player,move, matriz):
        from estados import Mapa as map
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
    
    
class Combate:

    def atualizar(self,jogo):
        self.printinfo(jogo)


    def printinfo(self,jogo):
        print()
        print("#")
        print()
        print(f"A vida do inimigo é {jogo.inimigo.vida}")
        print(f"Sua vida é {jogo.jogador.hp}")
        print("1. Atacar  2. Fugir  3. Conversar")
        escolha = input("Qual opção")
        match escolha:
            case "1":
                self.atacar(jogo, jogo.inimigo.vida)
            case "2":
                self.fugir(jogo)
            case "3":
                self.conversar(jogo)
    
    def atacar(self, jogo, vidaInimigo):
        vidaInimigo -= jogo.jogador.inventario[0].dano
        jogo.inimigo.vida = vidaInimigo
        print("inimigo atacado com sucesso")
        if jogo.inimigo.vida <= 0:
            print(f"Você derrotou o {jogo.inimigo.nome}")
            jogo.estado = Movimento()

    def fugir(self,jogo):
        print("Você conseguio fugir.")
        jogo.estado = Movimento()


    def conversar(self,jogo):
        print(jogo.inimigo.conversa)

