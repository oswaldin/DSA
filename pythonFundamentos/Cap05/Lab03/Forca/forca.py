# Encoding: UTF-8
# ========== Jogo da Forca =============

import random
import os

headerForca = '    +-----+\n    |     |'
middleForca = ['\n          |\n          |\n          |',
               '\n    O     |\n          |\n          |',
               '\n    O     |\n    |     |\n          |',
               '\n    O     |\n   /|     |\n          |',
               '\n    O     |\n   /|\\    |\n          |',
               '\n    O     |\n   /|\\    |\n   /      |',
               '\n    O     |\n   /|\\    |\n   / \\    |']
bottomForca = '\n          |\n          |\n====================='
mensagensPositivas = ['Boa tentativa!', 'Mandou bem!', 'Vamos lá', 'Incrível!', 'É isso aí!', 'Sensacional!', 'Você é demais!']
mensagensNegativas = ['Ops!', 'Eita, essa não tem!', 'Não desista', 'Tá difícil?', 'O que é isso, coleguinha?!', 'Errrrrrou!!!', 'Hehehe... deu não!']

class Forca():

    def __init__(self):
        self.contaErros = 0
        f = open('palavras.txt', 'r')
        palavras = f.read().split('\n')
        f.close
        self.palavra = random.choice(palavras).upper()
        self.palavraMascarada = list('_' * len(self.palavra))
        self.letrasErradas = []
        self.letrasCertas = []
        self.estado = 'vivo'
        self.mensagem = 'Boa sorte!'

    def renderiza(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n************************* Jogo da Forca **************************\n")
        print(headerForca + middleForca[self.contaErros] + bottomForca)
        print('\nLetras Erradas  : ', ' '.join(self.letrasErradas))
        print('Letras Corretas : ', ' '.join(self.letrasCertas))
        print('\nPalavra         : ', ' '.join(self.palavraMascarada))
        print('\n==============>>> ', self.mensagem)
        print('\n------------------------------------------------------------------')

    def confereletra(self, letra):
        if letra == '':
            self.mensagem = 'Tem que digitar uma letra, amiguinho!'
        else:
            letra = letra[0]
            if self.letrasCertas.count(letra) > 0 or self.letrasErradas.count(letra) > 0:
                self.mensagem = 'Tente outra letra... esta já foi antes'
            else:
                if self.palavra.count(letra) > 0:
                    for j in [i for i, x in enumerate(self.palavra) if x == letra]:
                        self.palavraMascarada[j] = letra
                    self.letrasCertas.append(letra)
                    self.mensagem = random.choice(mensagensPositivas)
                else:
                    self.contaErros += 1
                    self.letrasErradas.append(letra)
                    self.mensagem = random.choice(mensagensNegativas)
    def conferepalavra(self):
        if self.contaErros >= 6:
            self.estado = 'morto'
            self.mensagem = 'Que pena... suas chances acabaram. A palavra era ' + self.palavra
        else:
            if self.palavraMascarada.count('_') > 0:
                self.estado = 'vivo'
            else:
                self.estado = 'victory'
                self.mensagem = 'Parabéns! Você acertou! Yeah!!!!'


##================ Loop de execução da aplicação ===========================
fim = fimRodada = False

while fim == False:
    f = Forca()
    f.renderiza()
    while fimRodada == False:
        letra = (input('Escolha uma letra: ').upper())
        f.confereletra(letra)
        f.conferepalavra()
        f.renderiza()
        if f.estado == 'morto' or f.estado == 'victory':
            break
        else:
            continue
    continua = (input('Deseja jogar novamente (S/N)? ')).upper()
    if continua == 'S':
        continue
    else:
        break
print('\n\nMuito obrigado por jogar conosco. Até a próxima!')