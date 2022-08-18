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
print('Quiz: Avaliação de valores ético-morais aplicados.')
print('A seguir serão apresentadas 10 questões que abordam temas éticos-morais.')
print('Escolha a alternativa que lhe pareça o mais adequado para a situação apresentada.\n')
print('OBS: Neste quiz, se errar uma questão por falta de experiência ou identificação com a situação apresentada, não significará necessariamente que é uma pessoa ruim, mas que tem muito a aprender ainda na vida.')
print("_________________________________________________________________________________________________________")

print('1º pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('2º pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1
    
print('3º pergunta')
p3=perguntas(aleatorio())
if p3:
    pontos+=1

print('4º pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('5º pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1
    
print('6º pergunta')
p3=perguntas(aleatorio())
if p3:
    pontos+=1

print('7º pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('8º pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1
    
print('9º pergunta')
p1=perguntas(aleatorio())
if p1:
    pontos+=1

print('10º pergunta')
p2=perguntas(aleatorio())
if p2:
    pontos+=1


if pontos==10 or pontos==9:
    print('9-10')
    print('os nossos sistemas parabenizarão o jogador, devido a excentricidade de encontrar seres humanos carregando conhecimentos, experiências e responsabilidades desse nível, exaltando seu potencial de aproveitar esses ensinamentos e promover a difusão deles a todos que puderem com o objetivo de alcançar sociedades com menos ódio e violência ilógicos, seja na internet, seja em brigas de trânsito.')
elif pontos==8 or pontos==7:
    print('7-8')
    print('PARABÉNS! Você é do bem')
elif pontos==6 or pontos==5:
    print('5-6')
    print('Parabéns! Ao completar esse teste, vimos que você tem potencial para se tornar uma pessoa bem melhor')
elif pontos==4 or pontos==3:
    print('3-4')
    print('vejamos que você é uma pessoa de princípios pessoais fortes, mas mundanas')
else:
    print('0-2')
    print('Parabéns, obrigado por ceder seu tempo ao teste e a repensar sobre as ações que você toma com familiares, amigos ou estranhos. Prezamos que, por favor, reflita seriamente sobre o que andou aprendendo durante a vida, sobre as influências que você recebe, e de quem você influencia ou afeta com essas ideias')
    


    





