"# -Din-mica-Interativa-Personagens-do-Reino
# 🎮 Sistema de Personagens em Python com POO

## 🧑‍🏫 Introdução

Hoje vamos apresentar um exemplo de **Programação Orientada a Objetos em Python**, usando um sistema simples de RPG com personagens que usam:

- Classes e herança
- Sobrescrita de métodos (`override`)
- `super()` para reaproveitar funcionalidades

---

## 🧱 Classe Base: `Personagem`

```python
class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        print(f"{self.nome} ataca com força!")

    def subir_nivel(self):
        self.nivel += 1
        print(f"{self.nome} subiu para o nível {self.nivel}!")
```

### ✔ Explicação:
- Classe genérica para todos os personagens
- `__init__` define o nome e o nível
- `atacar()` é uma ação comum
- `subir_nivel()` aumenta o nível em +1

---

## ⚔️ Classe: `Guerreiro`

```python
class Guerreiro(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma

    def atacar(self):
        print(f"{self.nome} ataca com sua {self.arma}!")
```

### ✔ Explicação:
- Herda de `Personagem`
- Adiciona o atributo `arma`
- Reescreve o método `atacar()`

---

## 🔮 Classe: `Mago`

```python
class Mago(Personagem):
    def __init__(self, nome, nivel, magia):
        super().__init__(nome, nivel)
        self.magia = magia

    def atacar(self):
        super().atacar()
        print(f"{self.nome} lança a magia {self.magia}!")
```

### ✔ Explicação:
- Também herda de `Personagem`
- Usa `super().atacar()` para manter a ação da classe base
- Depois, executa sua própria ação mágica

---

## 🏹 Classe: `Arqueiro`

```python
class Arqueiro(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma

    def atacar(self):
        print(f"{self.nome} dispara uma flecha com seu(a) {self.arma}!")
```

---

## 🧪 Teste de Personagens

```python
g = Guerreiro("Gairadus, *𝖕𝖆𝖑𝖆𝖉𝖎𝖓𝖔 𝖉𝖆 𝖆𝖑𝖎𝖆𝖓ç𝖆*", 5, "Espada Longa")
m = Mago("Lissandryx, *𝖋𝖊𝖎𝖙𝖎𝖈𝖊𝖎𝖗𝖆 𝖈𝖔𝖓𝖉𝖊𝖓𝖆𝖉𝖆*", 7, "Bola de Fogo")
a = Arqueiro("Eldegran, *𝖆𝖗𝖖𝖚𝖊𝖎𝖗𝖔 𝖉𝖎𝖆𝖇ó𝖑𝖎𝖈𝖔*", 10, "Flecha envenenada")

g.atacar()
g.subir_nivel()
m.atacar()
m.subir_nivel()
a.subir_nivel()
a.atacar()
```

---

## 🖥️ Saída esperada:

```
Gairadus, *𝖕𝖆𝖑𝖆𝖉𝖎𝖓𝖔 𝖉𝖆 𝖆𝖑𝖎𝖆𝖓ç𝖆* ataca com sua Espada Longa!
Gairadus, *𝖕𝖆𝖑𝖆𝖉𝖎𝖓𝖔 𝖉𝖆 𝖆𝖑𝖎𝖆𝖓ç𝖆* subiu para o nível 6!
Lissandryx, *𝖋𝖊𝖎𝖙𝖎𝖈𝖊𝖎𝖗𝖆 𝖈𝖔𝖓𝖉𝖊𝖓𝖆𝖉𝖆* ataca com força!
Lissandryx, *𝖋𝖊𝖎𝖙𝖎𝖈𝖊𝖎𝖗𝖆 𝖈𝖔𝖓𝖉𝖊𝖓𝖆𝖉𝖆* lança a magia Bola de Fogo!
Lissandryx, *𝖋𝖊𝖎𝖙𝖎𝖈𝖊𝖎𝖗𝖆 𝖈𝖔𝖓𝖉𝖊𝖓𝖆𝖉𝖆* subiu para o nível 8!
Eldegran, *𝖆𝖗𝖖𝖚𝖊𝖎𝖗𝖔 𝖉𝖎𝖆𝖇ó𝖑𝖎𝖈𝖔* subiu para o nível 11!
Eldegran, *𝖆𝖗𝖖𝖚𝖊𝖎𝖗𝖔 𝖉𝖎𝖆𝖇ó𝖑𝖎𝖈𝖔* dispara uma flecha com seu(a) Flecha envenenada!
```

---

## ✅ Conclusão

- Usamos **herança** para reaproveitar código entre classes
- Aplicamos **sobrescrita de métodos** para personalizar comportamentos
- Utilizamos `super()` para **combinar o comportamento da classe base com o novo**
- Criamos um sistema pronto para evoluir para um mini-RPG!

---

## 💡 Dica: Próximos passos

- Adicionar pontos de vida e dano
- Fazer batalhas por turno
- Implementar uma interface de texto com `input()` para interagir com os personagens
