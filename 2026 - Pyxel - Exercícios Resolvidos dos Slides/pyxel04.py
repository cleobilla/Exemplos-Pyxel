import pyxel


class Circulo:
    # Construtor
    def __init__(self, x, y, raio):
        # Atributos
        self.cx = x
        self.cy = y
        self.raio = raio
        self.cor = 7

    # Métodos
    def desenha(self):
        pyxel.circ(self.cx, self.cy, self.raio, self.cor)

    def move(self, dx, dy):
        self.cx = self.cx + dx
        self.cy = self.cy + dy


class Janela:
    # Construtor
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura


class Jogo:
    # Construtor
    def __init__(self):
        # Atributos
        self.jan = Janela(90, 80)
        self.bola = Circulo(10, 20, 4)

        # Cria Janela
        pyxel.init(self.jan.largura, self.jan.altura)

        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        # Inicializa o deslocamento da bola
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

        # Atualiza a posição da bola
        self.bola.move(dx, dy)

        # Testa colisão da bola com as bordas da janela, se a bola encostar na borda da janela, corrige a posição da bola
        if self.bola.cx + self.bola.raio > self.jan.largura - 1: # -1 porque o pixel da borda direita da janela é o 89, começa no 0
            self.bola.cx = self.jan.largura - 1 - self.bola.raio
        if self.bola.cx - self.bola.raio < 0:
            self.bola.cx = self.bola.raio
        if self.bola.cy + self.bola.raio > self.jan.altura - 1: # -1 porque o pixel da borda inferior da janela é o 79, começa no 0
            self.bola.cy = self.jan.altura - 1 - self.bola.raio
        if self.bola.cy - self.bola.raio < 0:
            self.bola.cy = self.bola.raio

    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)

        # Desenha o objeto bola
        self.bola.desenha()


Jogo()
