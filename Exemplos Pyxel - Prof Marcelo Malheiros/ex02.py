import pyxel

class MouseApp:
    # Classe principal que desenha um círculo na posição do clique do mouse

    def __init__(self):
        # Inicializa a aplicação Pyxel e inicia o loop principal
        pyxel.init(100, 100, title='Hello')
        # Mostra o cursor do Mouse
        # pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        # Sem lógica de atualização neste caso
        pass

    def draw(self):
        # pyxel.cls(0)
        # Desenha um círculo na posição do clique do mouse
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, 10, 7)

# Instancia a aplicação
MouseApp()
