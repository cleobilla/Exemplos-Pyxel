import pyxel

class Fim:
    def __init__(self,x1,y1,largura,altura):
        self.x1 = x1
        self.y1 = y1
        self.largura = largura
        self.altura = altura
        self.cor = 15

class Parede:
    # Construtor
    def __init__(self, x1,y1,largura,altura):
        # Atributos
        self.x1 = x1
        self.y1 = y1
        self.largura = largura
        self.altura = altura
        self.cor = 9


class Gato:
    # Construtor
    def __init__(self, x,y):
        # Atributos
        self.x1 = x
        self.y1 = y
        # cat_16x16.png
        self.largura = 16
        self.altura = 16
        
    # Métodos
    def move(self,dx,dy):
        self.x1 = self.x1 + dx
        self.y1 = self.y1 + dy
        

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
        self.gato = Gato(10,20)
                
        self.paredes=[]
        #Borda superior
        self.paredes.append(Parede(0,0,self.jan.largura,1))
        #Borda inferior
        self.paredes.append(Parede(0,self.jan.altura-1,self.jan.largura,1))
        #Borda esquerda
        self.paredes.append(Parede(0,0,1,self.jan.altura))
        #Borda direita
        self.paredes.append(Parede(self.jan.largura-1,0,1,self.jan.altura))
        # Paredes centrais 
        self.paredes.append(Parede(self.jan.largura//3,0,1,60))
        self.paredes.append(Parede(self.jan.largura * 2/3,self.jan.altura-60,1,60))

        self.Fim = Fim(self.jan.largura - 20,self.jan.altura - 20,10,10)

        # Cria Janela
        pyxel.init(self.jan.largura,self.jan.altura)
        
        # Carregar imagens (entre pyxel.init e pyxel.run)
        pyxel.image(0).load(0, 0, 'cat_16x16.png')
        
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
            if self.colisao(self.gato,dx,dy,parede):
                move = False
        if move:
            self.gato.move(dx,dy)
            
    # Testa a colisão da bola com deslocamento com uma parede
    def colisao(self,rect1,dx,dy,rect2):
        # Limites da bola
        rect1_esq = rect1.x1 + dx
        rect1_dir = rect1.x1 + rect1.largura + dx
        rect1_top = rect1.y1 + dy
        rect1_dow = rect1.y1 + rect1.altura + dy
        
        # Limites da parede
        rect2_esq = rect2.x1 
        rect2_dir = rect2.x1 + rect2.largura
        rect2_top = rect2.y1 
        rect2_dow = rect2.y1 + rect2.altura
        
        # Bola ultrapassa limites das paredes?
        if (rect1_dir >= rect2_esq and
            rect1_esq <= rect2_dir and
            rect1_top <= rect2_dow and
            rect1_dow >= rect2_top):
            return True

        return False
            
            


    def draw(self):
        # Pinta a janela de preto (limpa a tela)
        pyxel.cls(0)
        
        # Desenha o objeto gato
        # Se o gato fosse um retângulo:
        # pyxel.rect(self.gato.x1,self.gato.y1,self.gato.largura,self.gato.altura,7)
        # Desenhando a imagem (sprite) carregada no init
        # Desenha o sprite
        # Note que ele inverte o densenho quando necessário.
        #     blt(           x,            y, img, u, v,  w,  h, corFundo)
        pyxel.blt(self.gato.x1, self.gato.y1, 0  , 0, 0, 16, 16,       13)

        
        # Desenha as paredes
        for parede in self.paredes:
               pyxel.rect(parede.x1,parede.y1,parede.largura,parede.altura,parede.cor)
        
        pyxel.rect(self.Fim.x1,self.Fim.y1,self.Fim.largura,self.Fim.altura,self.Fim.cor)
        
        if self.colisao(self.gato,0,0,self.Fim):
            pyxel.text(self.jan.largura//3,self.jan.altura//2,"You Win",15)


Jogo()




