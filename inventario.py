import os
import time

class Inventario:
    def atualizar(self,jogo):
        from movimentoEcombate import Movimento
        self.showInventario(jogo.jogador)
        jogo.estado = Movimento()
        

    def showInventario(self,player):
        import keyboard
        

        selecao = 0
        while True:
            os.system('cls')
            j = 0
            for i, item in enumerate(player.inventario):
                if i == selecao:
                    print(f"==> {item.nome}")
                    j += 1
                else:
                    print(f'    {item.nome}')
                    j += 1
            
            choice = keyboard.read_key()


            if choice == "s":
                selecao += 1
            elif choice == "w":
                selecao -= 1
            elif choice == 'enter':
                player.equipamento = player.inventario[selecao]
                print('equipamento equipado')
                break

            selecao = max(0, min(selecao, len(player.inventario)-1))

            time.sleep(0.5)
    
        