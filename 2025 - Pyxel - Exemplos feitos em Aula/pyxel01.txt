import pyxel

class Jogo:
    def __init__(self):
        pyxel.init(80, 100, title="Jogo")      
        # ULTIMA LINHA
        pyxel.run(self.update, self.draw)
    def update(self):
        pass
    def draw(self):
        pyxel.cls(0)
          	
Jogo()
