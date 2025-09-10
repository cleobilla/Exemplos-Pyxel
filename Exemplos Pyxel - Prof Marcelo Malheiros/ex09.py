import pyxel

class Personagem:
    # Classe para gerenciar o personagem
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.quadro = 0
        self.estado = 'direita'
        self.direita = [0, 14, 28, 42]  # Sprites para o movimento à direita
        self.esquerda = [0, 14, 28, 42]  # Sprites para o movimento à esquerda

    def mover(self):
        # Atualiza o estado e posição do personagem com base nas teclas pressionadas
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.estado = 'direita'
            self.x += 4
            self.quadro = (self.quadro + 1) % 4
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.estado = 'esquerda'
            self.x -= 4
            self.quadro = (self.quadro + 1) % 4

    def desenhar(self):
        # Desenha o personagem baseado no estado e no quadro atual
        if self.estado == 'direita':
            pyxel.blt(self.x, self.y, 0, self.direita[self.quadro], 54, 14, 18, 7)
        else:
            pyxel.blt(self.x, self.y, 0, self.esquerda[self.quadro], 36, 14, 18, 7)


class Jogo:
    # Classe principal do jogo
    def __init__(self):
        # Inicializa o Pyxel e o personagem
        pyxel.init(100, 100, title='Hello', fps=10)
        pyxel.image(0).load(0, 0, 'personagem_56x72.png')
        self.personagem = Personagem(50, 50)  # Cria o personagem
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo, delegando a movimentação ao personagem
        self.personagem.mover()

    def draw(self):
        # Desenha o fundo e o personagem
        pyxel.cls(1)
        self.personagem.desenhar()


# Instancia a aplicação
Jogo()
