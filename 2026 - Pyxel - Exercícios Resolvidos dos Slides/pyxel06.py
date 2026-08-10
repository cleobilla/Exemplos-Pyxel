import pyxel

class Goal:
    def __init__(self,x1,y1,largura,altura):
        # Atributos
        self.x1 = x1
        self.y1 = y1
        self.largura = largura
        self.altura = altura
        self.cor = 15
        self.criarBox()
    # Métodos

    def criarBox(self):
        self.x2 = self.x1 + self.largura - 1 # Largura é o número de pixels, como começa do zero tem que subtrair 1 para achar a coordenada do último pixel
        self.y2 = self.y1 + self.altura - 1 # Altura é o número de pixels, como começa do zero tem que subtrair 1 para achar a coordenada do último pixel

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
        self.criarBox()

    def criarBox(self):
        self.x2 = self.x1 + self.largura - 1 # Largura é o número de pixels, como começa do zero tem que subtrair 1 para achar a coordenada do último pixel
        self.y2 = self.y1 + self.altura - 1 # Altura é o número de pixels, como começa do zero tem que subtrair 1 para achar a coordenada do último pixel
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
        self.criarBox()

    def criarBox(self):
        self.x1 = self.x - self.raio
        self.y1 = self.y - self.raio
        self.x2 = self.x + self.raio
        self.y2 = self.y + self.raio
    # Métodos
    def desenha(self):
        pyxel.circ(self.x,self.y,self.raio,self.cor)

    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
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
        self.janela = Janela(90,80)
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
        self.paredes.append(Parede(self.janela.largura//3,0,2,60))
        self.paredes.append(Parede((self.janela.largura * 2)//3,self.janela.altura-60,2,60))

        # Cria o objeto fim da classe Goal, indicando o fim do labirinto.
        self.fim = Goal(self.janela.largura - 20,self.janela.altura - 20,10,10)
        
        # Cria janelaela
        pyxel.init(self.janela.largura,self.janela.altura)
        
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
        # Pinta a janelaela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto bola
        self.bola.desenha()
        
        # Desenha as paredes
        for parede in self.paredes:
            parede.desenha()
            
        self.fim.desenha()
        
        if self.colisao(self.bola,self.fim):
            pyxel.text(self.janela.largura//3,self.janela.altura//2,"You Win",15)


Jogo()



