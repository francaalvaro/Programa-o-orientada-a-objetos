from datetime import datetime


class Pessoa:
    # def falar(self):  # método do classe
    #     print('Pessoa está falando')
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):  # função com seus parametros
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
        if self.falando:
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = True

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
