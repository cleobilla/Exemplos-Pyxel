import pyxel

class Personagem:
    # Classe para representar o jogador
    def __init__(self, x, y, largura, altura, velocidade, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade
        self.cor = cor
        

    def mover(self):
        # Atualiza a posição do personagem com base nas teclas pressionadas
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.velocidade
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.velocidade
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.velocidade
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.velocidade

    def verificar_colisao(self, obstaculo):
        # Verifica colisão entre o personagem (Retangulo) e o obstáculo (retângulo)
        #personagem
        EsquerdaPersonagem = self.x
        DireitaPersonagem = self.x + self.largura
        SuperiorPersonagem = self.y
        InferiorPersonagem = self.y + self.altura

        #obstaculo
        EsquerdaObstaculo = obstaculo.x
        DireitaObstaculo = obstaculo.x + obstaculo.largura
        SuperiorObstaculo = obstaculo.y
        InferiorObstaculo = obstaculo.y + obstaculo.altura


        if (DireitaPersonagem > EsquerdaObstaculo and                
            EsquerdaPersonagem < DireitaObstaculo and 
            InferiorPersonagem > SuperiorObstaculo and
            SuperiorPersonagem < InferiorObstaculo):
            return True
        else:
            False
    
    def desenhar(self):
        # Desenha o personagem na tela
        pyxel.rect(self.x, self.y, self.largura, self.altura, self.cor)


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
        self.personagem = Personagem(80, 60, 4, 4, 1, 4)  # Inicializa o jogador
        self.obstaculo = Obstaculo(50, 50, 20, 5, 1)  # Inicializa o obstáculo como retângulo
        self.colidiu = False # Variável de controle de colisão
        pyxel.init(160, 120, title="Jogo com Obstáculo")
        pyxel.run(self.update, self.draw)



    def update(self):
        # Atualiza o estado do jogo
        self.personagem.mover()
        self.colidiu = self.personagem.verificar_colisao(self.obstaculo)

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(12)
        
        self.obstaculo.desenhar()
        self.personagem.desenhar()
        
        if self.colidiu:
            pyxel.text(60, 25, 'Colidiu', 8)


# Inicializa o jogo
Jogo()
