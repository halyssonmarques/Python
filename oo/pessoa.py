class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list (filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__== '__main__':
  python = Pessoa(nome='python')
  luciano = Pessoa(python, nome='Luciano')
  print(Pessoa.cumprimentar(luciano))
  print(id(luciano))
  print(luciano.cumprimentar())
  print(luciano.nome)
  print(luciano.idade)
  for filho in luciano.filhos:
      print(filho.nome)
      luciano.sobrenome = 'Ramalho'
      del luciano.filhos
      print(luciano.__dict__)
      print(python.__dict__)
      Pessoa.olhos = 3
      print(Pessoa.olhos)
      print(python.olhos)
      print(id(Pessoa.olhos), id(luciano.olhos), id(python.olhos))

