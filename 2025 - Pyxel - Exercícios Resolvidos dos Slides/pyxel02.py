import pyxel

class Circulo:
    #Construtor
    def __init__(self, x,y,raio):
        
        # Atributos
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = 7
        self.dx = 1 # deslocamento de x, velocidade de x ou derivada de x (posição)
        
    # Métodos
    def desenha(self):
        pyxel.circ(self.x,self.y,self.raio,self.cor)

    def mover(self):
        self.x = self.x + self.dx
        

class Jogo:
    # Constrututor
    def __init__(self):
    
        # Cria Janela com 160x120 pixels
        pyxel.init(160, 120)
        
        #Atributos
        self.bola = Circulo(10,20,5) # Cria o objeto Bola da classe Círculo

        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)
    
    # Métodos
    def update(self):
        # Lógica do Jogo
        self.bola.mover()

    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        self.bola.desenha()
Jogo()