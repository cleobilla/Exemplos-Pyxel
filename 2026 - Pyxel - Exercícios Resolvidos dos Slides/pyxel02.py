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

    def mover(self, dx, dy):
        self.cx = self.cx + dx
        self.cy = self.cy + dy


class Jogo:
    # Constrututor
    def __init__(self):

        # Cria Janela com 160x120 pixels
        pyxel.init(160, 120)

        # Atributos
        self.bola = Circulo(10, 20, 4)  # Cria o objeto Bola da classe Círculo

        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        # Lógica do Jogo
        self.bola.mover(1, 0)

    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)

        # Desenha o objeto bola
        self.bola.desenha()


Jogo()
