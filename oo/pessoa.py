class Pessoa:
    def __init__(selfn nome= None, idade=35):
        self.idade = idade
        self.nome = None
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__== '__main__':
     p = Pessoa()
     print(Pessoa.cumprimentar(p))
     print(id(p))
     print(p.cumprimentar())
     print(p.nome)
     p.nome = 'python'
     print(p.nome)
     print(p.idade)
