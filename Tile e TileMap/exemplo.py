import pyxel


# DEFINIR CONSTANTES PARA CÓDIGO FICA MAIS LEGÍVEL
TILE_SIZE = 8 # Valor padrão para a pyxel

# PARA NÃO COMPARAR VALORES NUMÉRICOS, DAR NOME AOS TILES
# BASEADO NA POSIÇÃO DOS TILES NO CANTO INFERIOR DIREITO DO PYXEL EDIT
PLATAFORMA = (2,0)
COIN = (5,0)


class Jogador:
    def __init__(self):
        self.x       = 0 
        self.y       = 5.9
        self.largura = 1 
        self.altura  = 1
        self.cor = 7
        self.chao = True
        self.vy = 0
        self.x_ant = self.x
        self.y_ant = self.y

    def move(self,dx,dy):
        self.x_ant = self.x
        self.y_ant = self.y
        self.x = self.x + dx
        self.y = self.y + dy
        
    def undo_move(self):
        self.x = self.x_ant
        self.y = self.y_ant
        
    def desenha(self):
        x = self.x * TILE_SIZE
        y = self.y * TILE_SIZE
        largura = self.largura * TILE_SIZE
        altura =  self.altura * TILE_SIZE
        cor = self.cor
        pyxel.rect(x,y,largura,altura,cor)

class Plataforma:
    def __init__(self,x,y):
        self.tile = PLATAFORMA
        self.x = x
        self.y = y
        self.largura = 1 
        self.altura = 1
        
class Moeda:
    def __init__(self,x,y):
        self.tile = COIN
        self.x = x
        self.y = y
        self.largura = 1
        self.altura = 1

class Jogo:
    def __init__(self):
        pyxel.init(8*TILE_SIZE,8*TILE_SIZE)
        pyxel.load("novo.pyxres")

        self.p = Jogador()
        self.plataformas = []
        self.moedas = []

        for tile_y in range(0,8):
            for tile_x in range(0,8):
                #print (pyxel.tilemaps[0].pget(tile_x, tile_y)," ",end='')
                if pyxel.tilemaps[0].pget(tile_x, tile_y) == COIN:
                    tile = "COIN"
                    c = Moeda(tile_x,tile_y)
                    self.moedas.append(c)
                elif pyxel.tilemaps[0].pget(tile_x, tile_y) == PLATAFORMA:
                    tile = "PLAT"
                    p = Plataforma(tile_x,tile_y)
                    self.plataformas.append(p)
                else:
                    tile = "    "
                print(tile," ",end="")
            print()

        pyxel.run(self.update,self.draw)

    def update(self):
        gravidade = 0.1
        dx = 0
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -0.1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx = 0.1
        if pyxel.btn(pyxel.KEY_UP) and self.p.chao == True:
            self.p.vy = -1
            self.p.chao = False
                
        self.p.vy = self.p.vy + gravidade
        self.p.move(dx,self.p.vy)

        print("Antes ",self.p.y)
        for plataforma in self.plataformas:
            if self.colisao(self.p,plataforma):
                self.p.undo_move()      
        print("Depois",self.p.y)

    def colisao(self,r1,r2): # colisao dois retangulos
        r1_esq = r1.x
        r1_dir = r1.x+r1.largura
        r1_top = r1.y
        r1_bas = r1.y+r1.altura
        
        r2_esq = r2.x
        r2_dir = r2.x+r2.largura
        r2_top = r2.y
        r2_bas = r2.y+r2.altura
        
        if (r1_dir >= r2_esq and r1_esq <= r1_dir and
            r1_top <= r2_bas and r1_bas >= r2_top):
            return True
        return False
    
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,8 * TILE_SIZE,8 * TILE_SIZE)
        self.p.desenha()

        
Jogo()