import pyxel

class Personagem:
    # Classe para gerenciar o personagem
    def __init__(self, x, y, sprites):
        self.x = x
        self.y = y
        self.sprites = sprites  # Lista de posições dos sprites
        self.sprite_index = 0  # Índice do sprite atual

    def mover(self):
        # Alterna entre os sprites para criar a animação
        self.sprite_index = (self.sprite_index + 1) % len(self.sprites)

        # Movimenta para a direita, verificando colisão com a cor 2
        if pyxel.pget(self.x + 8, self.y) != 2:
            self.x += 2

    def desenhar(self):
        # Desenha o personagem com o sprite atual
        pyxel.blt(self.x, self.y, 0, self.sprites[self.sprite_index], 0, 8, 8, 0)


class Obstaculo:
    # Classe para gerenciar o obstáculo
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = 2

    def desenhar(self):
        # Desenha o obstáculo como um retângulo
        pyxel.rect(self.x, self.y, self.x + self.largura, self.y + self.altura, self.cor)


class CollisionApp:
    # Classe principal do jogo

    def __init__(self):
        # Inicializa a aplicação Pyxel e os objetos do jogo
        pyxel.init(100, 100, title='Hello', fps=10)
        pyxel.image(0).load(0, 0, 'noguchi_128x128.png')
        
        # Criação do personagem
        # 32 e 40 são as posições no banco de imagens 0
        self.personagem = Personagem(50, 50, [32, 40])
        
        # Criação do obstáculo
        self.obstaculo = Obstaculo(90, 0, 10, 100)
        
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza a lógica do jogo
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.personagem.mover()

    def draw(self):
        # Desenha o cenário e os objetos do jogo
        pyxel.cls(1)
        self.obstaculo.desenhar()
        self.personagem.desenhar()

# Instancia a aplicação
CollisionApp()
