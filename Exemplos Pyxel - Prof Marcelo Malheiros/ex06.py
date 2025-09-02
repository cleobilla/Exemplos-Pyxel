import pyxel

class Personagem:
    # Classe para representar o jogador
    def __init__(self, x, y, raio, cor):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor

    def mover(self):
        # Atualiza a posição do personagem com base nas teclas pressionadas
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2

    def desenhar(self):
        # Desenha o personagem na tela
        pyxel.circ(self.x, self.y, self.raio, self.cor)


class Obstaculo:
    # Classe para representar o obstáculo como um retângulo
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def desenhar(self):
        # Desenha o retângulo na tela
        pyxel.rect(self.x, self.y, self.largura, self.altura, self.cor)


class Jogo:
    # Classe principal do jogo
    def __init__(self):
        self.personagem = Personagem(80, 60, 4, 9)  # Inicializa o jogador
        self.obstaculo = Obstaculo(50, 50, 20, 5, 8)  # Inicializa o obstáculo como retângulo
        pyxel.init(160, 120, title="Jogo com Obstáculo")
        pyxel.run(self.update, self.draw)

    def verificar_colisao(self):
        # Verifica colisão entre o personagem (círculo) e o obstáculo (retângulo)
        if (self.personagem.x + self.personagem.raio > self.obstaculo.x and
            self.personagem.x - self.personagem.raio < self.obstaculo.x + self.obstaculo.largura and
            self.personagem.y + self.personagem.raio > self.obstaculo.y and
            self.personagem.y - self.personagem.raio < self.obstaculo.y + self.obstaculo.altura):
            print("Colisão!")

    def update(self):
        # Atualiza o estado do jogo
        self.personagem.mover()
        self.verificar_colisao()

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(0)
        self.personagem.desenhar()
        self.obstaculo.desenhar()


# Inicializa o jogo
Jogo()
