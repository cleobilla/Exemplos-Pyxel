# Criar Classe Personagem
class Personagem:
    def __init__(self, nome, ataque, defesa):
        # Atributos
        self.nome = nome
        self.vida = 100
        self.ataque = ataque
        self.defesa = defesa
    def mostrar(self):
        print("Nome:",self.nome,"Vida:",self.vida)
    def aumentarAtaque(self):
        self.ataque = self.ataque + 10
        
    def atacar(self,inimigo):
        print(self.nome,"ataca",inimigo.nome)
        dano = self.ataque-inimigo.defesa
        print("Dano:",dano)
        if dano > 0:
            inimigo.vida = inimigo.vida-dano
heroi = Personagem("Luke",50,50)
heroi.mostrar()
vilao = Personagem("Darth Vader",60,40)
vilao.mostrar()
heroi.atacar(vilao)
vilao.mostrar()
vilao.atacar(heroi)
heroi.mostrar()

heroiNome = "assa"
heroiVida = 10
heroiAtaque = 100
heroi = ["aaad",10,100,50]

