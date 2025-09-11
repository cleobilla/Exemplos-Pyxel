import pyxel

class HelloPyxelApp:
    # Classe principal que encapsula o jogo 'Hello Pyxel'

    def __init__(self):
        # Inicializa a aplicação Pyxel e inicia o loop principal
        pyxel.init(100, 100, title='Hello')
        pyxel.run(self.update, self.draw)

    def update(self):
        # Atualiza o estado do jogo (sem lógica de atualização neste caso)
        pass

    def draw(self):
        # Desenha os elementos na tela
        pyxel.cls(0)  # Limpa a tela com a cor de fundo (0 - preto)
        pyxel.text(25, 45, 'Hello, Pyxel!', 9)  # Desenha o texto animado


# Instancia a aplicação (e inicia automaticamente o jogo)
HelloPyxelApp()
