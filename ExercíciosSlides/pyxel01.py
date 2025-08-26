import pyxel

class Jogo:
    #Construtor
    def __init__(self):
        
        # Inicializa a pyxel criando uma janela 160x120
        pyxel.init(160, 120)
    
        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        pass

    def draw(self):
        # Pinta a janela de preto (apaga tudo)        
        pyxel.cls(0)
        
        # Desenha o círculo
        x = 10
        y = 20
        raio = 5
        cor = 7
        pyxel.circ(x,y,raio,cor)

# Executa o construtor da classe Jogo
Jogo()
