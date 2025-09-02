import pyxel


class Personagem:
    # Classe para representar o jogador
    def __init__(self, x, y, velocidade):
        # Inicializa o personagem com posição, dimensões, velocidade e estado inicial
        self.x = x
        self.y = y
        self.largura = 17  # Dimensão fixa para largura
        self.altura = 17   # Dimensão fixa para altura
        self.velocidade = velocidade
        self.estado = "parado"  # Estado atual do personagem
        self.direcao = "direita"  # Direção inicial
        self.frame = 0  # Controla o quadro atual da animação
        self.posU = 0  # Coordenada X na imagem para desenhar o quadro correspondente

    def mover(self):
        # Movimenta o personagem e atualiza a direção
        if pyxel.btn(pyxel.KEY_LEFT):  # Move para a esquerda
            self.direcao = "esquerda"
            self.x -= self.velocidade
        elif pyxel.btn(pyxel.KEY_RIGHT):  # Move para a direita
            self.direcao = "direita"
            self.x += self.velocidade

    def desenhar(self):
        if self.estado == "parado":
            # Determina o tamanho do sprite com base na direção
            if self.direcao == "direita":
                self.tamanhoSprite = 17
            elif self.direcao == "esquerda":
                self.tamanhoSprite = -17  # Sprite espelhado para esquerda

            # Avança para o próximo quadro da animação
            self.frame += 1
            if self.frame > 7:  # Reseta ao completar a animação
                self.frame = 0
                #self.posU = 0
            
            # Desenha o quadro atual do personagem
            pyxel.blt(self.x, self.y, 0, 17 * self.frame, 0, self.tamanhoSprite, 17, 2)


class Jogo:
    # Classe principal do jogo
    def __init__(self):
        # Inicializa a janela e carrega os recursos
        pyxel.init(160, 120, fps=10, title="Animações")  # Tela de 160x120, 10 FPS
        pyxel.image(0).load(0, 0, "spritesGatinhosExpandido.png")  # Sprites com dimensões uniformes
        
        # Cria o personagem no jogo
        self.gatinho = Personagem(70, 100 - 17, 1)  # Começa na posição (70, 83)

        # Inicia o loop principal do jogo
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo
        self.gatinho.mover()

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(12)  # Limpa a tela com a cor de fundo
        pyxel.rect(0, 100, 200, 100, 14)  # Desenha o "chão"
        self.gatinho.desenhar()


# Inicializa o jogo
Jogo()
