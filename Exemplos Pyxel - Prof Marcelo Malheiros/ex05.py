import pyxel

class Personagem:
    def __init__(self, x, y, velocidade):
        # Inicializa o personagem com posição e velocidade.
        self.x = x
        self.y = y
        self.velocidade = velocidade

    def mover(self):
        #  Atualiza a posição do personagem com base nas teclas pressionadas.
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidade
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidade
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidade
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidade

    def desenhar(self):
        # Desenha o personagem na tela.
        pyxel.circ(self.x, self.y, 4, 9)  # Cor 9 = Azul


class Jogo:
    def __init__(self):
        # Inicializa o jogo, incluindo a tela e o personagem.
        pyxel.init(160, 120, title="Exemplo com Classes: Pyxel")
        self.jogador = Personagem(x=80, y=60, velocidade=2)  # Cria o jogador
        pyxel.run(self.atualizar, self.desenhar)

    def atualizar(self):
        # Atualiza o estado do jogo.
        self.jogador.mover()

    def desenhar(self):
        # Desenha os elementos do jogo.
        pyxel.cls(0)  # Limpa a tela com cor preta
        self.jogador.desenhar()


# Executa o jogo
Jogo()
