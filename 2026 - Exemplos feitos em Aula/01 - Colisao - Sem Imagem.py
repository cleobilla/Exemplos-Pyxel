import pyxel
class Personagem:
    def __init__(self,x,y,altura,largura,cor):
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
        pyxel.rect(self.x1,self.y1,self.largura,self.altura,self.cor)
                  

class Jogo:
    def __init__(self):
        pyxel.init(120,100,"Colisao")
        # Atributos aqui
        self.heroi = Personagem(10,10,5,5,7)
        self.inimigo = Personagem(80,80,10,10,10)
        
               
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
        self.mover(self.inimigo,pyxel.KEY_W ,pyxel.KEY_S   ,pyxel.KEY_A   ,pyxel.KEY_D)
        
        if self.colisao(self.heroi,self.inimigo):
            self.heroi.cor=8
        else:
            self.heroi.cor=7
        
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
        self.inimigo.draw()
Jogo()
    
    