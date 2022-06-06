class Pessoa:
    # def falar(self):  # método do classe
    #     print('Pessoa está falando')
    def __init__(self, nome, idade, comendo=False, falando=False):  # função com seus parametros
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
