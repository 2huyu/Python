import random

numeros=[0,1,2,3,4,5,6,7,8,9]
alternativas=['a','b','c','d','e']
numeros_usados=[]
pontos=0

def perguntas(num):
    if num == 0:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 1:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 2:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 3:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 4:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 5:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 6:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 7:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 8:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito
    elif num == 9:
        gabarito = False
        print(f'pegunta...')
        print('A...')
        print('B...')
        print('C...')
        print('D...')
        print('E...')
        alternativa=input('Alternativa escolhida: ').lower()
        while alternativa not in alternativas:
            alternativa=input('Alternativa escolhida (digite uma alternativa valida): ').lower()
        print('\n\n')
        if alternativa == 'c':
            gabarito=True
        return gabarito

def aleatorio():
    teste=True
    while teste:
        num_aleatorio=random.choice(numeros)
        if num_aleatorio in numeros_usados:
            continue
        else:
            teste=False
    numeros_usados.append(num_aleatorio)
    return num_aleatorio
    
print('--------------------------------------------------------------------------------------------------')
print('Quiz: Avalia????o de valores ??tico-morais aplicados.')
print('A seguir ser??o apresentadas 10 quest??es que abordam temas ??ticos-morais.')
print('Escolha a alternativa que lhe pare??a o mais adequado para a situa????o apresentada.\n')
print('OBS: Neste quiz, se errar uma quest??o por falta de experi??ncia ou identifica????o com a situa????o apresentada, n??o significar?? necessariamente que ?? uma pessoa ruim, mas que tem muito a aprender ainda na vida.')
print("_________________________________________________________________________________________________________")

print('1?? pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('2?? pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1
    
print('3?? pergunta')
p3=perguntas(aleatorio())
if p3:
    pontos+=1

print('4?? pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('5?? pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1
    
print('6?? pergunta')
p3=perguntas(aleatorio())
if p3:
    pontos+=1

print('7?? pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('8?? pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1
    
print('9?? pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('10?? pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1


if pontos==10 or pontos==9:
    print('9-10')
    print('os nossos sistemas parabenizar??o o jogador, devido a excentricidade de encontrar seres humanos carregando conhecimentos, experi??ncias e responsabilidades desse n??vel, exaltando seu potencial de aproveitar esses ensinamentos e promover a difus??o deles a todos que puderem com o objetivo de alcan??ar sociedades com menos ??dio e viol??ncia il??gicos, seja na internet, seja em brigas de tr??nsito.')
elif pontos==8 or pontos==7:
    print('7-8')
    print('PARAB??NS! Voc?? ?? do bem')
elif pontos==6 or pontos==5:
    print('5-6')
    print('Parab??ns! Ao completar esse teste, vimos que voc?? tem potencial para se tornar uma pessoa bem melhor')
elif pontos==4 or pontos==3:
    print('3-4')
    print('vejamos que voc?? ?? uma pessoa de princ??pios pessoais fortes, mas mundanas')
else:
    print('0-2')
    print('Parab??ns, obrigado por ceder seu tempo ao teste e a repensar sobre as a????es que voc?? toma com familiares, amigos ou estranhos. Prezamos que, por favor, reflita seriamente sobre o que andou aprendendo durante a vida, sobre as influ??ncias que voc?? recebe, e de quem voc?? influencia ou afeta com essas ideias')
    


    





