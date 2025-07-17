class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        print(f"{self.nome} ataca com força!")

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nome} subiu para o nível {self.nivel}!")
        
        
class Guerreiro(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma
    def atacar(self):
        print(f"{self.nome} ataca com sua {self.arma}!")
        
        
class Mago(Personagem):
    def __init__(self, nome, nivel, magia):
        super().__init__(nome, nivel)
        self.magia = magia

    def atacar(self):
        super().atacar()  # chama o método da classe pai (Personagem)
        print(f"{self.nome} lança a magia {self.magia}!")


        
class Arqueiro(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma

    def atacar(self):
        print(f"{self.nome} dispara uma flecha com seu(a) {self.arma}!")

        
g = Guerreiro("Gairadus, *𝖕𝖆𝖑𝖆𝖉𝖎𝖓𝖔 𝖉𝖆 𝖆𝖑𝖎𝖆𝖓ç𝖆*", 5, "Espada Longa")
m = Mago("Lissandryx, *𝖋𝖊𝖎𝖙𝖎𝖈𝖊𝖎𝖗𝖆 𝖈𝖔𝖓𝖉𝖊𝖓𝖆𝖉𝖆*", 7, "Bola de Fogo")
a= Arqueiro("Eldegran, *𝖆𝖗𝖖𝖚𝖊𝖎𝖗𝖔 𝖉𝖎𝖆𝖇ó𝖑𝖎𝖈𝖔*", 10, "Flecha envenenada")
g.atacar()
g.subir_nivel()
m.atacar()
m.subir_nivel()
a.subir_nivel()
a.atacar()