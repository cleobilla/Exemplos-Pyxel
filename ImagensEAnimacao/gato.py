import pyxel

class Goal:
    # Construtor
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


class Personagem:
    # Construtor
    def __init__(self, x,y):
        # Atributos
        self.x1 = x
        self.y1 = y
        # cat_16x16.png
        self.largura = 16
        self.altura = 16        
    # Métodos
    def desenha(self):
        # Desenha o objeto personagem
        # Se o personagem fosse um retângulo:
        # pyxel.rect(self.x1,self.y1,self.largura,self.altura,7)
        # Desenhando a imagem (sprite) carregada no init
        # Desenha o sprite
        # pyxel.blt(      x,       y, img, u, v, w           ,h          , corFundo)
          pyxel.blt(self.x1, self.y1, 0  , 0, 0, self.largura,self.altura, 13)
        
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
        self.janela = Janela(90,80)
        self.gato = Personagem(10,20)
              
        # Cria bordas e paredes internas e coloca numa lista
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
        self.paredes.append(Parede(self.janela.largura * 2/3,self.janela.altura-60,1,60))

        self.fim = Goal(self.janela.largura - 20,self.janela.altura - 20,10,10)

        # Cria janela
        pyxel.init(self.janela.largura,self.janela.altura)
        
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
            
    # Testa a colisão de um retângulo+(dx,dy) com outro retângulo
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
            return True # Se houve colisão retorna True

        # Se não houve colisão retorna False
        return False
            

    def draw(self):
        # Pinta a janelaela de preto (limpa a tela)
        pyxel.cls(0)

        # Desenha o objeto gato da classe personagem
        self.gato.desenha()
        
        # Desenha o objeto fim da classe Goal
        self.fim.desenha()
        
        # Desenha as paredes
        for parede in self.paredes:
            parede.desenha()
        
        # Verifica se gato colidiu com fim. Ganhou o jogo.
        if self.colisao(self.gato,0,0,self.fim):
            pyxel.text(self.janela.largura//3,self.janela.altura//2,"You Win",15)

Jogo()




