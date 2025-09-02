import pyxel
class Personagem:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.largura = 14
        self.altura = 18
        self.x_mem = 0
        self.contX = 0
        self.y_mem = 0
        self.contY = 0
       
    def move(self,dx,dy):
        self.x_mem = self.contX * self.largura
        self.contX = (self.contX + 1) % 4
        
        if dy > 0: # Indo para baixo, linha 0
            self.contY = 0
        if dy < 0: # Indo para cima, linha 1
            self.contY = 1
        if dx > 0: # Indo para dir, linha 0
            self.contY = 3
        if dx < 0: # Indo para esq, linha 1
            self.contY = 2
        self.y_mem = self.contY * self.altura
        
        self.x = self.x + dx
        self.y = self.y + dy
    def desenha(self):
        pyxel.blt(self.x,self.y,0,self.x_mem,self.y_mem,self.largura,self.altura,7)

class Parede:
    def __init__(self,x,y,largura,altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = 9
    def desenha(self):
        pyxel.rect(self.x,self.y,self.largura,self.altura,self.cor)

class Labirinto:
    def __init__(self):
        self.c = Personagem(10,10)        
        # Largura das paredes = 5
        self.paredes = []
        # Cria bordas
        borda_esq = Parede(0,0,5,100)
        self.paredes.append(borda_esq) 
        borda_dir = Parede(75,0,5,100) # 75 porque mais 5 tem que dar 80 que é a largura da jan.
        self.paredes.append(borda_dir)
        borda_top = Parede(0,0,80,5)
        self.paredes.append(borda_top)
        borda_bas = Parede(0,95,80,5) # 95 porque mais 5 tem que dar 100 que é a altura da jan.
        self.paredes.append(borda_bas)
        # Cria Obstáculos
        obs1 = Parede(80*1/3,0,5,70)
        self.paredes.append(obs1)
        obs2 = Parede(80*2/3,30,5,70)
        self.paredes.append(obs2)
        
        pyxel.init(80, 100, title="Jogo",fps=10)
        #CARREGAR IMAGENS
        pyxel.image(0).load(0,0,"personagem_56x72.png")        
        
        # ULTIMA LINHA
        pyxel.run(self.update, self.draw)

    def colisao(self,r1,r2):
        r1_dir = r1.x + r1.largura
        r1_esq = r1.x
        r1_base = r1.y + r1.altura
        r1_top = r1.y
    
        r2_esq = r2.x
        r2_dir = r2.x + r2.largura
        r2_top = r2.y
        r2_base = r2.y + r2.altura
        
        if (r1_dir >= r2_esq and
            r1_esq <= r2_dir and
            r1_base >= r2_top and
            r1_top <= r2_base):
            return True
        return False
        
    def update(self):
        dx = 0
        dy = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx = 4
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -4
        if pyxel.btn(pyxel.KEY_UP):
            dy = -4
        if pyxel.btn(pyxel.KEY_DOWN):
            dy = 4
        if dx!=0 or dy!=0:
            self.c.move(dx,dy)
            for parede in self.paredes:
                if self.colisao(self.c,parede):
                    self.c.move(-dx,-dy)
        
    def draw(self):
        pyxel.cls(0)
        # Desenha o círculo
        self.c.desenha()
        # Desenha paredes
        for parede in self.paredes:
            parede.desenha()
          	
Labirinto()
