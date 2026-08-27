import pyxel

class Inimigo:
    # Classe para gerenciar cada inimigo
    def __init__(self, x, y, velocidade_y):
        self.x = x
        self.y = y
        self.velocidade_y = velocidade_y

    def mover(self):
        # Atualiza a posição do inimigo
        self.y += self.velocidade_y
        if self.y > pyxel.height:
            self.y = -8

    def desenhar(self):
        # Desenha o inimigo na tela
        pyxel.blt(self.x, self.y, 0, 104, 40, 8, 8, 0)


class Jogo:
    # Classe principal do jogo
    def __init__(self):
        # Inicializa o Pyxel e cria os inimigos
        pyxel.init(100, 100, title='Hello', fps=30)
        pyxel.image(0).load(0, 0, 'noguchi_128x128.png')
        self.inimigos = [
            Inimigo(10, 20, 1),
            Inimigo(43, 52, 3),
            Inimigo(87, 11, 2)
        ]
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo, delegando o movimento para cada inimigo
        for inimigo in self.inimigos:
            inimigo.mover()

    def draw(self):
        # Desenha o fundo e os inimigos
        pyxel.cls(0)
        for inimigo in self.inimigos:
            inimigo.desenhar()


# Instancia a aplicação
Jogo()
