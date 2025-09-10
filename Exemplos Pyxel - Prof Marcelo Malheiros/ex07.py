import pyxel

class Gato:
    # Classe que representa o gato animado
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def atualizar_posicao(self):
        # Atualiza a posição do gato e inverte a direção se atingir as bordas
        self.x += self.vx
        self.y += self.vy
        if self.x < 0 or self.x >= 84:
            self.vx = -self.vx
        if self.y < 0 or self.y >= 84:
            self.vy = -self.vy

    def desenhar(self):   
        # Desenha o sprite
        # Note que ele inverte o densenho quando necessário.
        #     blt(     x,      y, img, u, v,                w        ,  h, [colkey], [rotate], [scale])
        pyxel.blt(self.x, self.y, 0  , 0, 0, 16 * pyxel.sgn(-self.vx), 16,       13,       30,     0.8)



class BouncingApp:
    # Classe principal com o jogo

    def __init__(self):
        # Inicializa a aplicação Pyxel e inicia o loop principal
        pyxel.init(100, 100, title='Hello')
        # Aqui carrega a imagem (arquivo) para o banco de imagem(0). Pyxel tem 3 bancos de imagem de 256 x 256.
        pyxel.image(0).load(0, 0, 'cat_16x16.png')
        # Instancia o gato
        self.gato = Gato(50, 20, 2, 1)
        
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo (movimento do gato)
        self.gato.atualizar_posicao()

    def draw(self):
        # Desenha o fundo e o gato
        pyxel.cls(1)
        self.gato.desenhar()

# Instancia a aplicação
BouncingApp()
