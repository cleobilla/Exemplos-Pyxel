import pyxel

class AnimatedApp:
    # Classe principal com movimento animado de um retângulo

    def __init__(self):
        # Inicializa a aplicação Pyxel e inicia o loop principal
        pyxel.init(100, 100, title='Hello')
        self.x = 10
        self.y = 20  # Posições iniciais do retângulo
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza as posições animadas do retângulo
        self.x = (self.x + 3.1) % pyxel.width
        self.y = (self.y + 1.4) % pyxel.height

    def draw(self):
        # Desenha o retângulo animado
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, 3, 3, 9)

# Instancia a aplicação
AnimatedApp()
