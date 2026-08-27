import pyxel
class Personagem:
    def __init__(self,x,y,largura,altura,cor):
        self.x1=x
        self.y1=y
        self.largura=largura
        self.altura=altura
        self.cor = cor
        self.definirBox()
        
    def definirBox(self):
        self.x2 = self.x1 + abs(self.largura)
        self.y2 = self.y1 + abs(self.altura)
    
    def mover(self,dx,dy):
        self.x1 = self.x1 + dx
        self.y1 = self.y1 + dy
        self.definirBox()
        
    def draw(self):
        pyxel.blt(self.x1, self.y1,             # Posição na tela
                  0,                            # qual das imagens (matrizes) que pyxel disponibiliza: 0, 1 ou 2.
                  0,0,                          # posição da imagem na matriz
                  self.largura, self.altura,    # largura e altura da imagem
                  self.cor)                     # cor do fundo que é transparente
                  

class Jogo:
    def __init__(self):
        pyxel.init(120,100,"Colisao")
        # Atributos aqui
        self.heroi = Personagem(10,10,14,18,7)
        
        #Carregar imagem
        pyxel.images[0].load(0, 0, "personagem_56x72.png")
        
               
        pyxel.run(self.update,self.draw)
    
    def mover(self,obj,up,down,left,right):
        dx=0
        dy=0
        if pyxel.btn(up):
            dy = -1
        if pyxel.btn(down):
            dy = +1
        if pyxel.btn(left):
            dx = -1
        if pyxel.btn(right):
            dx = +1
        obj.mover(dx,dy)
         
    def update(self):
        self.mover(self.heroi  ,pyxel.KEY_UP,pyxel.KEY_DOWN,pyxel.KEY_LEFT,pyxel.KEY_RIGHT)
                  
    def colisao(self,obj1,obj2):
        
        colisaoX = (obj2.x1 <= obj1.x1 and obj1.x1 <= obj2.x2) or (obj2.x1 <= obj1.x2 and obj1.x2 <= obj2.x2)
        colisaoY = (obj2.y1 <= obj1.y1 and obj1.y1 <= obj2.y2) or (obj2.y1 <= obj1.y2 and obj1.y2 <= obj2.y2)
        if colisaoX and colisaoY:
            return True
        else:
            return False
        
   
    def draw(self):
        pyxel.cls(0)
        self.heroi.draw()
Jogo()
    
    