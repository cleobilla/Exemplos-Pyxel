import pyxel


class Personagem:
    # Classe para representar o jogador
    def __init__(self, x, y, velocidade):
        # Inicializa o personagem com posição, dimensões, velocidade e estado inicial
        self.x = x
        self.y = y
        self.largura = 17  # Dimensão fixa para largura no estado "parado"
        self.altura = 17   # Dimensão fixa para altura no estado "parado"
        self.velocidade = velocidade
        self.estado = "parado"  # Estado inicial ("parado" ou "andando")
        self.direcao = "direita"  # Direção inicial do personagem
        self.frame = 0  # Controla o quadro atual da animação
        self.posU = 0  # Coordenada X no sprite sheet

    def mover(self):
        # Controla o movimento do personagem e atualiza seu estado
        if pyxel.btn(pyxel.KEY_LEFT):  # Movendo para a esquerda
            self.estado = "andando"
            self.direcao = "esquerda"
            self.x -= self.velocidade
        elif pyxel.btn(pyxel.KEY_RIGHT):  # Movendo para a direita
            self.estado = "andando"
            self.direcao = "direita"
            self.x += self.velocidade
        else:
            self.estado = "parado"  # Parado quando nenhuma tecla é pressionada

    def desenhar(self):
        if self.estado == "parado":  # Animação do estado parado
            if self.direcao == "direita":
                self.tamanhoSprite = 17
            elif self.direcao == "esquerda":
                self.tamanhoSprite = -17  # Espelha o sprite
            
            # Atualiza o quadro da animação
            self.frame += 1
            if self.frame > 7:  # Reseta após 8 quadros
                self.frame = 0
                self.posU = 0
            
            # Desenha o personagem parado
            pyxel.blt(self.x, self.y, 0, 17 * self.frame, 0, self.tamanhoSprite, 17, 2)

        elif self.estado == "andando":  # Animação do estado andando
            self.largura = 20  # Ajusta a largura para o sprite de "andando"
            if self.direcao == "direita":
                self.tamanhoSprite = 20
            elif self.direcao == "esquerda":
                self.tamanhoSprite = -20
            
            # Atualiza o quadro da animação
            self.frame += 1
            if self.frame > 7:  # Reseta após 8 quadros
                self.frame = 0
                self.posU = 0
            
            # Desenha o personagem andando (ajustando a altura do sprite)
            pyxel.blt(self.x, self.y + 4, 0, 20 * self.frame, 17, self.tamanhoSprite, 13, 2)


class Jogo:
    # Classe principal do jogo
    def __init__(self):
        # Inicializa a janela e carrega os recursos
        pyxel.init(160, 120, fps=10, title="Animações")  # Tela de 160x120, 10 FPS
        pyxel.image(0).load(0, 0, "spritesGatinhosExpandido.png")  # Sprites organizados por estados

        # Cria o personagem no jogo
        self.gatinho = Personagem(70, 100 - 17, 2)  # Posição inicial com velocidade 2

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
