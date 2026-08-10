import pyxel

class Parede:
    # Construtor
    def __init__(self, x1,y1,largura,altura):
        # Atributos
        self.x1 = x1
        self.y1 = y1
        self.largura = largura
        self.altura = altura
        self.cor = 9
        self.criarBox()
    # Métodos
    def criarBox(self): 
        self.x2 = self.x1 + self.largura - 1# Largura é o número de pixels, como começa do zero tem que subtrair 1 para achar a coordenada do último pixel
        self.y2 = self.y1 + self.altura  - 1 # Altura é o número de pixels, como começa do zero tem que subtrair 1 para achar a coordenada do último pixel

    
    def desenha(self):
        pyxel.rect(self.x1,self.y1,self.largura,self.altura,self.cor)


class Circulo:
    # Construtor
    def __init__(self, x,y,raio):
        # Atributos
        self.cx = x
        self.cy = y
        self.raio = raio
        self.cor = 7
        self.criarBox()

    def criarBox(self):
        self.x1 = self.cx - self.raio
        self.y1 = self.cy - self.raio
        self.x2 = self.cx + self.raio
        self.y2 = self.cy + self.raio
        
    # Métodos
    def desenha(self):
        pyxel.circ(self.cx,self.cy,self.raio,self.cor)

    def move(self,dx,dy):
        self.cx = self.cx + dx
        self.cy = self.cy + dy
        self.criarBox()
        

class Janela:
    # Construtor
    def __init__(self,largura, altura):
        self.largura = largura
        self.altura = altura

class Jogo:
    # Construtor
    def __init__(self):
        #Atributos
        self.jan = Janela(90,80)
        self.bola = Circulo(10,20,1)
                
        # Cria as bordas e a parede interna e coloca numa lista.
        self.paredes=[]
        #Borda superior
        self.paredes.append(Parede(0,0,self.jan.largura,1))
        #Borda inferior
        self.paredes.append(Parede(0,self.jan.altura-1,self.jan.largura,1))
        #Borda esquerda
        self.paredes.append(Parede(0,0,1,self.jan.altura))
        #Borda direita
        self.paredes.append(Parede(self.jan.largura-1,0,1,self.jan.altura))
        # Parede central
        self.paredes.append(Parede(self.jan.largura//2,0,1,60))

        # Cria Janela
        pyxel.init(self.jan.largura,self.jan.altura)
        
        ## Roda o Jogo (sempre última linha do __init__)
        pyxel.run(self.update, self.draw)

    # Métodos
    def update(self):
        # Testa se Bola pode ser movida antes de mover
        dx = 0
        dy = 0
        
        # Verifica o botão pressionado e verifica qual deslocamento fazer
        if pyxel.btn(pyxel.KEY_UP):
            dy = -1
        if pyxel.btn(pyxel.KEY_DOWN):
            dy = 1
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -1
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx = 1
        
        self.bola.move(dx,dy)

        for parede in self.paredes:
            if self.colisao(self.bola,parede):
                self.bola.move(-dx,-dy)
                print("aa")

    # Testa a colisão entre dois objetos
    def colisao(self,obj1,obj2):
        colisao_x = (
            (obj2.x1 <= obj1.x1 and obj1.x1 <= obj2.x2) or
            (obj2.x1 <= obj1.x2 and obj1.x2 <= obj2.x2)
        )
        colisao_y = (
            (obj2.y1 <= obj1.y1 and obj1.y1 <= obj2.y2) or
            (obj2.y1 <= obj1.y2 and obj1.y2 <= obj2.y2)
        )
        if colisao_x and colisao_y:
            return True
        else:
            return False

    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        self.bola.desenha()
        
        # Desenha as paredes
        for parede in self.paredes:
               parede.desenha()

Jogo()


