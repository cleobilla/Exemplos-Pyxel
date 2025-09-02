import pyxel


class Personagem:
    def __init__(self, x, y, velocidade):
        # Inicializa o personagem com posição, dimensões, velocidade e estado inicial
        self.x = x
        self.y = y
        self.largura = 17
        self.altura = 17
        self.velocidade = velocidade
        self.estado = "parado"  # Estado inicial ("parado", "andando", ou "pulando")
        self.direcao = "direita"  # Direção inicial do personagem
        self.frame = 0  # Controla o quadro atual da animação
        self.posU = 0  # Coordenada X no sprite sheet
        self.velocidade_vertical = 0  # Velocidade no eixo Y para o pulo
        self.no_chao = True  # Verifica se o personagem está no chão

    def mover(self):
        # Controla o movimento e atualiza o estado do personagem
        if pyxel.btn(pyxel.KEY_LEFT):
            if self.estado != "pulando":  # Evita alterar o estado durante o pulo
                self.estado = "andando"
            self.direcao = "esquerda"
            self.x -= self.velocidade
        elif pyxel.btn(pyxel.KEY_RIGHT):
            if self.estado != "pulando":
                self.estado = "andando"
            self.direcao = "direita"
            self.x += self.velocidade
        else:
            if self.estado != "pulando":
                self.estado = "parado"

        # Inicia o pulo se o personagem estiver no chão e a tecla de pulo for pressionada
        if pyxel.btnp(pyxel.KEY_UP) and self.no_chao:
            self.pular()

        # Atualiza a física do pulo (gravidade e movimento vertical)
        self.atualizar_pulo()

    def pular(self):
        # Configura os parâmetros para o pulo
        self.estado = "pulando"
        self.velocidade_vertical = -4  # Velocidade inicial do pulo (subida)
        self.frame = -1  # Reinicia o quadro da animação de pulo
        self.no_chao = False  # Personagem não está mais no chão

    def atualizar_pulo(self):
        # Gerencia a física do pulo
        if self.estado == "pulando":
            self.y += self.velocidade_vertical  # Atualiza a posição vertical
            self.velocidade_vertical += 0.5  # Aplica gravidade

            # Detecta o contato com o chão
            if self.y >= 100 - self.altura:
                self.y = 100 - self.altura  # Ajusta a posição no chão
                self.no_chao = True  # Permite pular novamente
                self.estado = "parado"  # Retorna ao estado parado

    def desenhar(self):
        if self.estado == "parado":
            # Animação e desenho do estado parado
            if self.direcao == "direita":
                self.tamanhoSprite = 17
            elif self.direcao == "esquerda":
                self.tamanhoSprite = -17

            self.frame += 1
            if self.frame > 7:
                self.frame = 0
                self.posU = 0
            pyxel.blt(self.x, self.y, 0, 17 * self.frame, 0, self.tamanhoSprite, 17, 2)
        
        elif self.estado == "andando":
            # Animação e desenho do estado andando
            self.largura = 20
            if self.direcao == "direita":
                self.tamanhoSprite = 20
            elif self.direcao == "esquerda":
                self.tamanhoSprite = -20

            self.frame += 1
            if self.frame > 7:
                self.frame = 0
                self.posU = 0
            pyxel.blt(self.x, self.y + 4, 0, 20 * self.frame, 17, self.tamanhoSprite, 13, 2)
        
        elif self.estado == "pulando":
            # Animação e desenho do estado pulando
            if self.direcao == "direita":
                self.tamanhoSprite = 19
            elif self.direcao == "esquerda":
                self.tamanhoSprite = -19

            # Controla os quadros da animação de pulo (baseado na velocidade vertical)
            if self.frame < 1 and self.velocidade_vertical < 0:
                self.frame += 1
            if self.frame < 4 and self.velocidade_vertical > 0:
                self.frame += 1

            pyxel.blt(self.x, self.y, 0, 19 * self.frame, 31, self.tamanhoSprite, 15, 2)


class Jogo:
    def __init__(self):
        pyxel.init(160, 120, fps=10, title="Animações")
        pyxel.image(0).load(0, 0, "spritesGatinhosExpandido.png")
        self.gatinho = Personagem(70, 100 - 17, 2)

        pyxel.run(self.update, self.draw)

    def update(self):
        self.gatinho.mover()

    def draw(self):
        pyxel.cls(12)
        pyxel.rect(0, 100, 200, 100, 14)
        self.gatinho.desenhar()


Jogo()
