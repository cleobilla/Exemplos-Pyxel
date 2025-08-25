import pyxel

class Circulo:
    # Construtor
    def __init__(self, x,y,raio):
        # Atributos
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = 7
        self.dx = 1 # deslocamento de x, velocidade de x ou derivada de x (posição)
    
    # Métodos
    def move(self):
        self.x = self.x + self.dx

    def inverteSentidoDx(self):
        self.dx = self.dx * (-1)


class Janela:
    # Construtor
    def __init__(self,largura, altura):
        self.largura = largura
        self.altura = altura

class Jogo:
    # Construtor
    def __init__(self):
        #Atributos
        self.jan = Janela(160,120)
        self.bola = Circulo(10,20,5)

        # Cria Janela
        pyxel.init(self.jan.largura,self.jan.altura)
        
        ## Roda o Jogo (sempre última linha do __init__
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        # Testa se Bola pode ser movida antes de mover
        if self.bola.x + self.bola.raio + self.bola.dx > self.jan.largura:
           self.bola.inverteSentidoDx()
        if self.bola.x - self.bola.raio + self.bola.dx < 0:
           self.bola.inverteSentidoDx()
        self.bola.move()
        
    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        pyxel.circ(self.bola.x,self.bola.y,self.bola.raio,self.bola.cor)

Jogo()
