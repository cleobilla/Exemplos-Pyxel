import pyxel
class Circulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.raio = 3
        self.cor = 7
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def desenha(self):
        pyxel.circ(self.x,self.y,self.raio,self.cor)

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
        self.c = Circulo(10,10)        
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
        
        pyxel.init(80, 100, title="Jogo")      
        # ULTIMA LINHA
        pyxel.run(self.update, self.draw)

    def colisao(self,circulo,retangulo):
        c_dir = circulo.x + circulo.raio
        c_esq = circulo.x - circulo.raio
        c_base = circulo.y + circulo.raio
        c_top = circulo.y - circulo.raio
    
        r_esq = retangulo.x
        r_dir = retangulo.x + retangulo.largura
        r_top = retangulo.y
        r_base = retangulo.y + retangulo.altura
        
        if (c_dir >= r_esq and
            c_esq <= r_dir and
            c_base >= r_top and
            c_top <= r_base):
            return True
        return False
        
    def update(self):
        dx = 0
        dy = 0
        if pyxel.btn(pyxel.KEY_RIGHT):
            dx = 1
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -1
        if pyxel.btn(pyxel.KEY_UP):
            dy = -1
        if pyxel.btn(pyxel.KEY_DOWN):
            dy = 1
            
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
