# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

import os
fim = False

som = lambda a,b : a + b
sub = lambda a,b : a - b
mlt = lambda a,b : a * b
div = lambda a,b : a / b


while fim == False:
    os.system('cls' if os.name == 'nt' else 'clear') 

    print("\n******************* Python Calculator *******************")
    print("\n Selecione o número da operação desejada:")
    print("\n")
    print("      1 - Soma")
    print("      2 - Subtração")
    print("      3 - Multiplicação")
    print("      4 - Divisão")
    print("      -----------------------")
    print("      X - Sair")

    o = input("\nDigite sua opção (1/2/3/4/X): ")
    if o == 'X' or o == 'x':
        fim == True
        break
    else:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

    if o == '1': 
        r = som(x,y)
    elif o == '2' : 
        r = sub(x,y)
    elif o == '3' : 
        r = mlt(x,y)
    elif o == '4' : 
        r = div(x,y)
    elif o == 'X' or o == 'x':
        fim = True
        break
    else:
        continue

    print("O resultado é %f" % (r))

    c = input("\n\nPressione [ENTER] para continuar...")

print('\n\nObrigado por utilizar nossa calculadora.py\n\n')