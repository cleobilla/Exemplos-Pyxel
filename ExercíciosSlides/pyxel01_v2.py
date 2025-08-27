import pyxel

class Circulo:
    # Construtor
    def __init__(self, x,y,raio):
        # Atributos
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = 7
    # Métodos
    def desenha(self):
        pyxel.circ(self.x,self.y,self.raio,self.cor)

class Jogo:
    # Construtor
    def __init__(self):
        # Inicializa a pyxel criando uma janela 160x120
        pyxel.init(160, 120)
        
        # Atributos
        # Cria o objeto Bola da classe Circulo (chama o construtor de Círculo)
        self.bola = Circulo(10,20,5)
        
        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        # Nada a fazer ainda.
        pass

    def draw(self):
        # Pinta toda a janela de preto (Limpa a tela)
        pyxel.cls(0)
        
        # Desenha a Bola
        self.bola.desenha()

Jogo()