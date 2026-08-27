import pyxel


class Circulo:
    # Construtor
    def __init__(self, x, y, raio):
        # Atributos
        self.cx = x
        self.cy = y
        self.raio = raio
        self.cor = 7
        self.dx = 1

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
        self.jan = Janela(160, 120)
        self.bola = Circulo(10, 20, 4)

        # Cria Janela
        pyxel.init(self.jan.largura, self.jan.altura)

        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):

        # Atualiza a posição da bola
        self.bola.move(self.bola.dx, 0)

        # Testa colisão da bola com as bordas da janela
        if (
            self.bola.cx + self.bola.raio >= self.jan.largura):  # Se a bola encostar na borda direita da janela
            # Corrige a posição da bola
            self.bola.cx = self.jan.largura - self.bola.raio
            # Inverte a direção da bola
            self.bola.dx = -1
        elif (
            self.bola.cx - self.bola.raio <= 0):  # Se a bola encostar na borda esquerda da janela
            # Corrige a posição da bola
            self.bola.cx = self.bola.raio
            # Inverte a direção da bola
            self.bola.dx = 1

    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)

        # Desenha o objeto bola
        self.bola.desenha()


Jogo()
