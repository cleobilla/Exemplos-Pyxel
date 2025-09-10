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





    def verifica_pode_andar(self, lista_obstaculos, direcao):
        # Verifica se o personagem pode andar sem colidir com nenhum obstáculo
        for obstaculo in lista_obstaculos:
            if not self._verifica_pode_andar_obstaculo(obstaculo, direcao):
                return False  # Colidiu com pelo menos um obstáculo
        return True
    
    def mover(self, lista_obstaculos):
        # Movimenta o personagem apenas se não houver colisão em nenhuma direção
        if pyxel.btn(pyxel.KEY_LEFT) and self.verifica_pode_andar(lista_obstaculos, "esquerda"):
            self.x -= self.velocidade
        if pyxel.btn(pyxel.KEY_RIGHT) and self.verifica_pode_andar(lista_obstaculos, "direita"):
            self.x += self.velocidade
        if pyxel.btn(pyxel.KEY_UP) and self.verifica_pode_andar(lista_obstaculos, "cima"):
            self.y -= self.velocidade
        if pyxel.btn(pyxel.KEY_DOWN) and self.verifica_pode_andar(lista_obstaculos, "baixo"):
            self.y += self.velocidade

    def _verifica_pode_andar_obstaculo(self, obstaculo, direcao):
        # Ajusta os limites do personagem com base na direção do movimento
        if direcao == "esquerda":
            EsquerdaPersonagem = self.x - self.velocidade
            DireitaPersonagem = self.x
            SuperiorPersonagem = self.y
            InferiorPersonagem = self.y + self.altura
        elif direcao == "direita":
            EsquerdaPersonagem = self.x + self.largura
            DireitaPersonagem = self.x + self.largura + self.velocidade
            SuperiorPersonagem = self.y
            InferiorPersonagem = self.y + self.altura
        elif direcao == "cima":
            EsquerdaPersonagem = self.x
            DireitaPersonagem = self.x + self.largura
            SuperiorPersonagem = self.y - self.velocidade
            InferiorPersonagem = self.y
        elif direcao == "baixo":
            EsquerdaPersonagem = self.x
            DireitaPersonagem = self.x + self.largura
            SuperiorPersonagem = self.y + self.altura
            InferiorPersonagem = self.y + self.altura + self.velocidade
        else:
            return True  # Caso nenhuma direção seja fornecida

        # Limites do obstáculo
        EsquerdaObstaculo = obstaculo.x
        DireitaObstaculo = obstaculo.x + obstaculo.largura
        SuperiorObstaculo = obstaculo.y
        InferiorObstaculo = obstaculo.y + obstaculo.altura

        # Verifica se há colisão
        if (DireitaPersonagem > EsquerdaObstaculo and                
            EsquerdaPersonagem < DireitaObstaculo and 
            InferiorPersonagem > SuperiorObstaculo and
            SuperiorPersonagem < InferiorObstaculo):
            return False
        return True

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
        self.obstaculo1 = Obstaculo(50, 50, 20, 5, 1)
        self.obstaculo2 = Obstaculo(110, 10, 30, 10, 1)
        self.obstaculo3 = Obstaculo(100, 50, 20, 30, 1)
        self.listaObstaculos = [self.obstaculo1, self.obstaculo2, self.obstaculo3]
        pyxel.init(160, 120, title="Jogo com Obstáculos")
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo
        self.personagem.mover(self.listaObstaculos)

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(12)
        for obstaculo in self.listaObstaculos:
            obstaculo.desenhar()
        self.personagem.desenhar()

        


# Inicializa o jogo
Jogo()
