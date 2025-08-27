import pyxel

class Goal:
    def __init__(self,x1,y1,largura,altura):
        self.x1 = x1
        self.y1 = y1
        self.largura = largura
        self.altura = altura
        self.cor = 15
    # Métodos
    def desenha(self):
        pyxel.rect(self.x1,self.y1,self.largura,self.altura,self.cor)


class Parede:
    # Construtor
    def __init__(self, x1,y1,largura,altura):
        # Atributos
        self.x1 = x1
        self.y1 = y1
        self.largura = largura
        self.altura = altura
        self.cor = 9
    # Métodos
    def desenha(self):
        pyxel.rect(self.x1,self.y1,self.largura,self.altura,self.cor)

class Circulo:
    # Construtor
    def __init__(self,x,y,raio):
        # Atributos
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = 7
        
    # Métodos
    def desenha(self):
        pyxel.circ(self.x,self.y,self.raio,self.cor)

    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
    
        

class janelaela:
    # Construtor
    def __init__(self,largura, altura):
        self.largura = largura
        self.altura = altura

class Jogo:
    # Construtor
    def __init__(self):
        #Atributos
        self.janela = janelaela(90,80)
        self.bola = Circulo(10,20,1)
               
        # Crias as bordas e as paredes internas e coloca numa lista
        self.paredes=[]
        #Borda superior
        self.paredes.append(Parede(0,0,self.janela.largura,1))
        #Borda inferior
        self.paredes.append(Parede(0,self.janela.altura-1,self.janela.largura,1))
        #Borda esquerda
        self.paredes.append(Parede(0,0,1,self.janela.altura))
        #Borda direita
        self.paredes.append(Parede(self.janela.largura-1,0,1,self.janela.altura))
        # Paredes centrais 
        self.paredes.append(Parede(self.janela.largura//3,0,1,60))
        self.paredes.append(Parede((self.janela.largura * 2)//3,self.janela.altura-60,1,60))

        # Cria o objeto fim da classe Goal, indicando o fim do labirinto.
        self.fim = Goal(self.janela.largura - 20,self.janela.altura - 20,10,10)
        
        # Cria janelaela
        pyxel.init(self.janela.largura,self.janela.altura)
        
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
        parede_dir = parede.x1 + parede.largura
        parede_top = parede.y1 
        parede_dow = parede.y1 + parede.altura
        
        # Bola ultrapassa limites das paredes?
        if (bola_dir >= parede_esq and
            bola_esq <= parede_dir and
            bola_top <= parede_dow and
            bola_dow >= parede_top):
            return True

        return False
            
            


    def draw(self):
        # Pinta a janelaela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        self.bola.desenha()
        
        # Desenha as paredes
        for parede in self.paredes:
            parede.desenha()
            
        self.fim.desenha()
        
        if self.colisao(self.bola,0,0,self.fim):
            pyxel.text(self.janela.largura//3,self.janela.altura//2,"You Win",15)


Jogo()



