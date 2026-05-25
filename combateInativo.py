'''from movimento import Movimento

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

    def fugir(self,jogo):
        print("Você conseguio fugir.")
        jogo.estado = Movimento()


    def conversar(self,jogo):
        print(jogo.inimigo.conversa)'''