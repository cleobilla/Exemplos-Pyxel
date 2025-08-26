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


class Circulo:
    # Construtor
    def __init__(self, x,y,raio):
        # Atributos
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = 7
        
    # Métodos
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
        

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
                
        self.paredes=[]
        #Borda superior
        self.paredes.append(Parede(0,0,self.jan.largura,1))
        #Borda inferior
        self.paredes.append(Parede(0,self.jan.altura-1,self.jan.largura,1))
        #Borda esquerda
        self.paredes.append(Parede(0,0,1,self.jan.altura))
        #Borda direita
        self.paredes.append(Parede(self.jan.largura,0,1,self.jan.altura))
        # Parede central
        self.paredes.append(Parede(self.jan.largura//2,0,1,60))

        # Cria Janela
        pyxel.init(self.jan.largura,self.jan.altura)
        
        ## Roda o Jogo (sempre última linha do __init__
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
        
        move = True
        for parede in self.paredes:
            if self.colisao(self.bola,dx,dy,parede):
                move = False
        if move:
            self.bola.move(dx,dy)

    # Testa a colisão da bola com deslocamento com uma parede
    def colisao(self,bola,dx,dy,parede):
        # Limites da bola
        bola_esq = bola.x-bola.raio+dx
        bola_dir = bola.x+bola.raio+dx
        bola_top = bola.y-bola.raio+dy
        bola_dow = bola.y+bola.raio+dy
        
        # Limites da parede
        parede_esq = parede.x1 
        parede_dir = parede.x1 + parede.largura - 1
        parede_top = parede.y1 
        parede_dow = parede.y1 + parede.altura - 1
        
        # Bola ultrapassa limites das paredes?
        if (bola_dir >= parede_esq and
            bola_esq <= parede_dir and
            bola_top <= parede_dow and
            bola_dow >= parede_top):
            return True

        return False
            
            


    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        pyxel.circ(self.bola.x,self.bola.y,self.bola.raio,self.bola.cor)
        
        # Desenha as paredes
        for parede in self.paredes:
               pyxel.rect(parede.x1,parede.y1,parede.largura,parede.altura,parede.cor)

Jogo()


