import pyxel

class Circulo:
    # Construtor
    def __init__(self, x,y,raio):
        # Atributos
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = 7
        
    # Métodos
    def desenha(self):
        pyxel.circ(self.x,self.y,self.raio,self.cor)

    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

class Janela:
    # Construtor
    def __init__(self,largura, altura):
        self.largura = largura
        self.altura = altura

class Jogo:
    # Construtor
    def __init__(self):
        #Atributos
        self.jan = Janela(90,80)
        self.bola = Circulo(10,20,5)

        # Cria Janela
        pyxel.init(self.jan.largura,self.jan.altura)
        
        ## Roda o Jogo (sempre última linha do __init__
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        # Testa se Bola pode ser movida antes de mover
        dx = 0
        dy = 0
        
        # Verifica o botão pressionado e verifica qual deslocamento fazer
        if pyxel.btn(pyxel.KEY_UP):
            dy = -1
        if pyxel.btn(pyxel.KEY_DOWN):
            dy = 1
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -1
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx = 1
        
        # Testa se ao aplicar o deslocamento a bola ainda fica dentro da tela.
        # Testa se bate na direita
        if self.bola.x+self.bola.raio+dx<self.jan.largura:
            # Testa se bate na esquerda
            if self.bola.x-self.bola.raio+dx>0:
                # Testa se bate em cima
                if self.bola.y-self.bola.raio+dy>0:
                    # Testa se bate embaixo
                    if self.bola.y+self.bola.raio+dy<self.jan.altura:   
                        self.bola.move(dx,dy)

    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        self.bola.desenha()

Jogo()

