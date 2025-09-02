import pyxel

class Game:
    def __init__(self):
        # Define o x e o y inicial do círculo
        self.x = 80
        self.y = 60
        # Cria janela 160x120
        pyxel.init(160, 120,title="Meu primeiro Jogo")
        # Inicializa o ciclo do jogo
        pyxel.run(self.update, self.draw)

    def update(self):
        # Movimenta o círculo de acordo com a tecla pressionada
        if pyxel.btn(pyxel.KEY_LEFT): self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT): self.x += 2
        if pyxel.btn(pyxel.KEY_UP): self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN): self.y += 2

    def draw(self):
        # Limpa a tela e pinta de preto (O)
        pyxel.cls(0)
        # Desenha o círculo na posição x,y. Ele tem raio 4 e cor 9 (laranja)
        pyxel.circ(self.x, self.y, 4, 9)

Game()
