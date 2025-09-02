import pyxel

class Personagem:
    # Classe para representar o jogador
    def __init__(self, x, y, velocidade):
        # Inicializa o personagem com posição, dimensões, velocidade e estado inicial
        self.x = x
        self.y = y
        self.largura = 16
        self.altura = 16
        self.velocidade = velocidade
        self.estado = "parado"  # Estado atual do personagem (por enquanto, apenas "parado")
        self.frame = 0  # Controla o quadro atual da animação
        self.posU = 0  # Coordenada X na imagem para desenhar o quadro correspondente

    def mover(self):
        # Movimenta o personagem apenas se as teclas de direção estiverem pressionadas
        if pyxel.btn(pyxel.KEY_LEFT):  # Move para a esquerda
            self.x -= self.velocidade
        if pyxel.btn(pyxel.KEY_RIGHT):  # Move para a direita
            self.x += self.velocidade

    def desenhar(self):
        if self.estado == "parado":
            # Define os tamanhos dos quadros da animação "parado"
            tamanhosX = [17, 17, 14, 13, 14, 14, 17, 17]
            
            # Incrementa a posição na imagem baseando-se no quadro atual
            self.posU += tamanhosX[self.frame]
            
            # Avança para o próximo quadro da animação
            self.frame += 1
            
            # Reseta a animação ao completar todos os quadros
            if self.frame > 7:
                self.frame = 0
                self.posU = 0
            
            # Desenha o quadro atual do personagem
            pyxel.blt(self.x, self.y, 0, self.posU, 0, tamanhosX[self.frame], 16, 2)


class Jogo:
    # Classe principal do jogo
    def __init__(self):
        # Inicializa a janela e carrega os recursos
        pyxel.init(160, 120, fps=10, title="Animações")  # Tela de 160x120, 10 FPS
        pyxel.image(0).load(0, 0, "spritesGatinhosColados.png")  # Carrega os sprites do gatinho
        
        # Cria o personagem no jogo
        self.gatinho = Personagem(70, 100 - 16, 1)  # Começa na posição (70, 84)

        # Inicia o loop principal do jogo
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo
        self.gatinho.mover()

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(6)  # Limpa a tela com a cor de fundo
        pyxel.rect(0, 100, 200, 100, 14)  # Desenha o "chão" (área verde)
        self.gatinho.desenhar()

# Inicializa o jogo
Jogo()

