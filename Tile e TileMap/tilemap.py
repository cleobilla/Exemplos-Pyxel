import pyxel


# DEFINIR CONSTANTES PARA CÓDIGO FICA MAIS LEGÍVEL
TILE_SIZE = 8 # Valor padrão para a pyxel

# PARA NÃO COMPARAR VALORES NUMÉRICOS, DAR NOME AOS TILES
# BASEADO NA POSIÇÃO DOS TILES NO CANTO INFERIOR DIREITO DO PYXEL EDIT
FUNDO  = (1,0)
PAREDE = (2,0)
MOEDA   = (5,0)


class Jogador:
    def __init__(self):
        self.x       = 0 
        self.y       = 6
        self.largura = 1 
        self.altura  = 1
        self.cor     = 7
        self.moedas  = 0
  
        # Usado para voltar o movimento, caso dê colisão
        self.x_ant   = self.x
        self.y_ant   = self.y


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

class Parede:
    def __init__(self,x,y):
        self.tile = PAREDE # Usa a constante para ficar mais legível, mas é igual ao valor (2,0)
        self.x = x
        self.y = y
        self.largura = 1 
        self.altura = 1
        
class Moeda:
    def __init__(self,x,y):
        self.tile = MOEDA # Usa a constante para ficar mais legível, mas é igual ao valor (5,0)
        self.x = x
        self.y = y
        self.largura = 1
        self.altura = 1

class Jogo:
    def __init__(self):

        self.tilemap_largura = 8
        self.tilemap_altura = 8
        
        pyxel.init(self.tilemap_largura*TILE_SIZE,self.tilemap_altura*TILE_SIZE)

        pyxel.load("novo.pyxres")
        self.mostraTileMap()

        self.p = Jogador()
        self.paredes = []
        self.moedas = []
        
        self.paredes = self.tilemapTotileList(Parede,PAREDE)
        self.moedas = self.tilemapTotileList(Moeda,MOEDA)

        pyxel.run(self.update,self.draw)
    
    # Função que lê o tilemap e preenche as listas de parede e moedas
    def mostraTileMap(self):
        for tile_y in range(0,self.tilemap_altura):
            for tile_x in range(0,self.tilemap_largura):
                if pyxel.tilemaps[0].pget(tile_x, tile_y) == MOEDA:
                    tile = "MOEDA"
                elif pyxel.tilemaps[0].pget(tile_x, tile_y) == PAREDE:
                    tile = "PARED"
                else:
                    tile = "    "
                print(tile," ",end="")
            print()
        # Função que lê o tilemap e preenche as listas de parede e moedas
    def tilemapTotileList(self,Classe,tile):
        L=[]
        for tile_y in range(0,self.tilemap_altura):
            for tile_x in range(0,self.tilemap_largura):
                if pyxel.tilemaps[0].pget(tile_x, tile_y) == tile:
                    L.append(Classe(tile_x,tile_y))
        return L

    def update(self):
        dx = 0
        dy = 0
        if pyxel.btn(pyxel.KEY_LEFT):
            dx = -0.1
        elif pyxel.btn(pyxel.KEY_RIGHT):
            dx = 0.1
        if pyxel.btn(pyxel.KEY_UP):
            dy = -0.1
        if pyxel.btn(pyxel.KEY_DOWN):
            dy = 0.1

        self.p.move(dx,dy)

        for parede in self.paredes:
            if self.colisao(self.p,parede):
                self.p.undo_move()
                
        moedas_copia = list(self.moedas) # list cria uma cópia da lista de moedas
        for moeda in moedas_copia:
            if self.colisao(self.p,moeda):
                self.p.moedas = self.p.moedas + 1
                print(self.p.moedas)
                
                pyxel.tilemaps[0].pset(moeda.x, moeda.y,FUNDO)
                
                self.moedas.remove(moeda) # remove da lista original
        

    def colisao(self,r1,r2): # colisao dois retangulos
        r1_esq = r1.x
        r1_dir = r1.x+r1.largura
        r1_top = r1.y
        r1_bas = r1.y+r1.altura
        
        r2_esq = r2.x
        r2_dir = r2.x+r2.largura
        r2_top = r2.y
        r2_bas = r2.y+r2.altura
        
        if (r1_dir > r2_esq and r1_esq < r2_dir and
            r1_top < r2_bas and r1_bas > r2_top):
            return True
        return False
    
    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,0,0,0,8 * TILE_SIZE,8 * TILE_SIZE)
        self.p.desenha()

        
Jogo()