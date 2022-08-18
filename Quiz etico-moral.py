from tkinter import *
import time
import random

# ----------------------------------------------------------------------------------------
# Desenvolvido por:
# Vítor Benvenisti Laguna Navarenho TIA: 32245637 email:32245637@mackenzista.com.br
# Zhuyu Chen Su TIA: 32212259 email:32212259@mackenzista.com.br
# Marcos Vinicius Ferreira Assis TIA: 32228953 email:32228953@mackenzista.com.br
# ----------------------------------------------------------------------------------------

#Abre a janela
window = Tk()
window.title("Quiz")
#Definindo tamanho da interface - INICIA
WIDTH, HEIGHT = 800, 400
window.resizable(False, False)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (WIDTH/2))
y_cordinate = int((screen_height/2) - (HEIGHT/2))

window.geometry(f"{WIDTH}x{HEIGHT}+{x_cordinate}+{y_cordinate - 20}")
#Definindo tamanho da interface - ACABA

#GRID da interface - INICIA
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)

window.rowconfigure(0, weight=2)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
#GRID da interface - ACABA


#Perguntas e gabarito - INICIA

pergunta1 = "Você está andando pela rua e encontra uma nota de 50$ no chão, você olha ao redor e procura algúem que possa ter perdido aquele dinheiro. Você percebe que uma mulher está desesperada vindo em sua direção olhando pela calçada a procura de algo, logo presume que o dinheiro é dela. Você sabe que ela não te viu e que se decidir sair dali com o dinheiro ninguém vai notar. Qual seria a sua atitude?"
pergunta2 = "É uma sexta feira, final de expediente e você depende de um colega de trabalho para terminar suas tarefas e poder ir embora. Seu colega não colaborou ainda, como você reagiria?"
pergunta3 = "Você está em uma praia incrível e se sente atraído por uma pessoa que está próximo a você. Você decide tentar contato, como você faz?"
pergunta4 = "Você passa por uma rua e percebe que um homem está agredindo uma mulher, o que você faz?"
pergunta5 = "Em seu trabalho, repercutiu-se a notícia de que uma das funcionárias tentou processar seu chefe por assédio sexual e de repente todos ficaram sabendo da especulação de que ela tentou um suborno ao forçar uma relação, mas que falhou e está tentando arruinar a vida do chefe. Você a conhece o suficiente para saber que não faria isso. A cada dia, ela parece estar cada vez mais destruída por dentro pela falsa acusação. O que fará?"
pergunta6 = "Ao voltar para casa, você se depara com dois homens brancos e um oriental brigando no trânsito, mas logo, percebeu que se desenvolveu por causa da discriminação étnica dos dois. Você tenta parar e acabam te hostilizando também, mas o oriental responde que não precisa de ajuda de um negro, logo, percebe que esse pequeno problema pode escalar gravemente, visto a faca no cinto de um deles. O que faz?"
pergunta7 = "Em um dia, reencontrou-se ao acaso com uma pessoa com quem teve desentendimentos e discussões há muitos anos atrás, gerando um ódio de anos. Então, a frequência de encontros com ela tem aumentado e sua aversão pela pessoa também, apesar de ela parecer diferente hoje em dia. O que fará?"
pergunta8 = "Você está na sala de aula e vê um garoto que é constantemente ignorado e às vezes até sofre de agressividade de outros grupos de alunos. Um dia você decide iniciar uma conversa com ele, mas logo descobre que possui um comportamento antipático e emocionalmente fechado, ofendendo-lhe e afastando-lhe. Porém, decide voltar para tirar satisfação, o que fará?"
pergunta9 = "Você está em seu primeiro trabalho, seus colegas são legais, o patrão demonstra comportamentos rígidos, mas todo o processo está cansando de forma extrema. Você vê que o índice de demissão voluntária só continua crescendo nos últimos anos e pensa no caso. Porém, sua família depende de sua resiliência e você não sabe se encontrará outro. O que fará?"
pergunta10 = "Você é um usuário de redes sociais e gosta de frequentar o Twitter para ver notícias. Você se depara com duas pessoas discutindo ideias absurdas e, logo, diversos cidadãos surgem para apoiar um dos lados. O que você faz?"

feedback0 = "Feedback: Confrontar judicialmente suas autoridades sem um plano é pedir para ser jogado no fundo do poço junto com a vítima. Desse jeito, vocês ficarão com traumas pelo restante da vida. E no caso dela, pode ser pior ainda, pois tipos como abuso sexual ou gaslighting (bem frequente entre familiares) deixam marcas psicológicas que assombram e ameaçam a sanidade e a segurança das vítimas. Ajude, com esperteza, quando perceber situações desse tipo a sua volta, antes que se torne uma tragédia."
feedback1 = "Feedback: Em quase todas as situações da vida, você verá que guardar rancor por alguém só cultiva uma angústia internamente, que pode até levar a uma depressão, sendo que poderia ser evitado se apenas procurasse compreender o outro lado ou superar. A vingança torna tudo pior ainda pois gera consequência externa. E talvez a pessoa simplesmente tivesse uma perspectiva de mundo diferente da sua e era imatura na época para respeitar sua visão. Pessoas podem mudar, dado as devidas explicações."
feedback2 = "Não é bom julgar o caráter do outro pela superfície. Pessoas com comportamentos assim podem aparentar passividade ou calmaria, mas suas mentes podem estar um turbilhão. Ou seja, essa pessoa pode estar com diversos problemas pessoais que levam à depressão, um problema grave e indiscriminado. Cada pessoa, deficiente ou saudável, rica ou opbre, pode desenvolvê-la a partir de suas próprias inseguranças e visões de mundo. Pode ser mais virtuoso resgatar alguém fora da ponte do que em cima dela."
feedback3 = "Feedback: Suportar e sobrepujar as mais diversas dores na vida também é querer o bem para si. Nem toda época difícil da vida significa que vai te destruir e que precisa fugir. Mas preste atenção: saiba separar quando está fazendo algo bem para si e sua família, a longo prazo, de quando está pondo sua saúde física e mental em risco, como suportar abusos sem reporte. Aproveite a juventude para, no futuro, desfrutar do que já passou e lutou."
feedback4 = "Feedback: Discussões e retóricas informais e ignorantes estão espalhadas no mundo todo em toda história. Logo, perder tempo ou se estressar, entrando em discussões, com esperança de mudar a vida do outro nessas mídias sociais pode te levar à bolhas sociais e prejudicar a si mesmo a longo prazo. Priorize quem se importa nesse caso. Na maioria das vezes, são apenas pessoas querendo afirmar sua superioridade por conta da moralidade subjetiva moderna(self)."
feedback5 = "Feedback: Tentar se envolver imprudentemente em brigas alheias não é uma boa ideia, principalmente se for para contribuir na disseminação de ódio. A conversa deve ser sempre a primeira forma e principal forma de resolver um assunto, procurar saber do outro lado antes de afirmar, de julgar. Nunca seja impulsivo, ainda mais quando a situação oferece risco à sua vida. Discriminação racial ou étnica não é aceitável, então apenas assistir é ser cúmplice também."

# Move para uma nova linha a cada n palavras.
def insert_newlines(s, n=15):
    a = s.split()
    ret = ''
    for i in range(0, len(a), n):
        ret += ' '.join(a[i:i+n]) + '\n'

    return ret

# Função que faz com que a ordem das questões sejam aleatórias.

numeros = [0,1,2,3,4,5,6,7,8,9]
numeros_usados = []
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

#Função que armazena todas as questões, suas alternativas e feedback para serem facilmente selecionadas
def perguntas(numero_da_pergunta):

    perguntas_alternativas_respostas = [
        #MODELO: [pergunta, alternativa_A, alternativa_B, alternativa_C, alternativa_D, alternativa_E, alternativa_correta, feedback]
        [f"{insert_newlines(pergunta1)}", "Achado não é roubado, ela que perdeu e eu não tenho nada a ver com isso. O dinheiro agora é meu.", "Não mexe no dinheiro e segue seu caminho sem falar nem fazer nada.", "Você anda até ela e pergunta o que ela está procurando, se ela estiver procurando uma nota de 50$ você entrega para ela.", "Você pega a nota de cinquenta reais e deixa uma nota qualquer de menor valor no lugar dela, na tentativa de minimizar a perda da mulher.", "Você pega a nota e sai correndo sem olhar para trás.", "C", "Feedback: Roubar nunca será a melhor escolha, sempre preze e faça pelos outros o que você gostaria que fizessem por você."],
        [f"{insert_newlines(pergunta2)}", "Iria até o setor desse colega e brigaria com ele independente de quem estivesse presente.", "Escreveria um e-mail para o seus superiores expondo as atitudes de seu colega.", "Iria embora sem resolver a tarefa e sem dar satisfação para ninguém.", "Procuraria esse colega e buscaria entender porque ele ainda não tinha te retornado.", "Ficaria no seu setor esperando o tempo que fosse necessário.", "D", "Feedback: A conversa deve ser sempre a primeira forma de tentar resolver um problema, nunca tome atitudes sem pensar ou por impulso."],
        [f"{insert_newlines(pergunta3)}", "Insiste, mesmo recebendo uma negativa, porque \"não\" é na verdade charme.", "Tenta causar um afogamento com a pessoa, para depois salvá-la e se tornar um herói.", "Invade o local onde ela está hospedada e aguarda com um presente legal.", "Tentar fazer contato de alguma forma, mas respeitando os limites e espera a pessoa corresponder.", "Tenta chamar atenção de formas inusitadas.", "D", "Feedback: Qualquer forma de tentar coagir uma pessoa a fim de que ela esteja com você é errado.\n Em uma boa relação existe acima de tudo o respeito."],
        [f"{insert_newlines(pergunta4)}", "\"Em briga de marido e mulher não se mete a colher\".Segue o seu caminho.", "Intervém, e tenta proteger a mulher e assim que possível chama a polícia.", "Avisa alguém que esteja próximo e segue seu caminho deixando a responsabilidade para outro.", "Liga para a polícia, mas não intervém na briga.", "Filma para postar na internet e compartilhar nos grupos de Whatsapp.", "B", "Feedback: Ficar em silêncio em uma situação de agressão física é ser cúmplice, assim como compartilhar videos violentos disseminando ódio.\n Procure sempre ajudar as pessoas a sua volta."],
        [f"{insert_newlines(pergunta5)}", "Com calma, você chega na conclusão de que infortúnios acontecem na vida e é melhor não se envolver no caso", "Intrigado, procura saber o que aconteceu junto com ela e rapidamente denuncia para a polícia o caso,\n iniciando um confronto judicial direto entre vocês e seu chefe", "Enfurecido, tenta contestar, sem um plano, contra os boatos de que o patrão é quem está errado,\n provocando conflitos internos no trabalho e criando inimigos", "Sem levantar suspeitas, procure saber o que aconteceu de fato entre eles, com conversas sinceras\n e planejamento para conseguir provas e reportar os envolvidos por gaslighting", "Indiferente, tenta consolar ela e aproveitar seu estado de vulnerabilidade para protegê-la e iniciar um romance", "D", f"{insert_newlines(feedback0)}"],
        [f"{insert_newlines(pergunta6)}", "Enfurecido, se junta aos xenofóbicos para dar uma lição no racista", "Com adrenalina no sangue, se junta ao oriental para uma luta justa em duplas.", "Você se afasta e cada um cuida da sua vida, esperando que algum deles aprenda a lição na marra", "Com calma, você xinga ambos para chamar a atenção deles e sai correndo e pedindo a ajuda mais próxima possível", "Você tenta mostrar que esse ódio racial é irracional e chama a polícia caso rejeitem", "E", f"{insert_newlines(feedback5)}"],
        [f"{insert_newlines(pergunta7)}", "Manter a relação de antipatia com ela.", " Criar uma relação de amizade forçada, mantendo seus sentimentos escondidos", "Decidir não suportar mais essa dor e cortar suas relações com ela.", "Se aproximar dela e criar um plano com outra pessoa para boicotar a vida dela.", "Não forçar uma amizade, mas conversar e compreender o porquê da pessoa ter sido daquele jeito", "E", f"{insert_newlines(feedback1)}"],
        [f"{insert_newlines(pergunta8)}", "Olhar com desprezo para o garoto e afirmar que não conseguirá nada na vida sendo desse jeito", "Conversar com ele, questionando-o de modo a pressioná-lo sobre o porquê de ser assim", "Chamar atenção dele para lhe olhar conversar com seus amigos para jogar na cara dele.", "Manter a calma, falar que está tudo bem e tentar entender o porquê dele ser assim ", "Ignorá-lo e deixá-lo continuar com sua a autodepreciação", "D", f"Feedback: {insert_newlines(feedback2)}"],
        [f"{insert_newlines(pergunta9)}", "Pedir demissão e passar pela incerteza de encontrar outro trabalho que ofereça algo melhor", "Suportar e tomar como experiência de vida e de competência para, então, trocar de emprego eventualmente", "Conversar com seu patrão e pedir aumento de salário sem estar há muito tempo no trabalho", "Conversar com seus colegas sobre sua situação e realizar um motim", " Realizar todo o trabalho e tudo que o patrão mandar, até pondo sua dignidade em risco", "B", f"{insert_newlines(feedback3)}"],
        [f"{insert_newlines(pergunta10)}", "Ignora a discussão e cada um cuida da sua vida", "Intervir com a abordagem da moralidade tecnoética a fim de mudar a cosmovisão digiespacial", "Intervir com sua opinião crítica a fim de mudar as outras pessoas e tornar o mundo melhor, mas ser atacado de volta", "Chamar a polícia para caçar os autores dos comentários pois estavam discutindo a ideia de haver um partido nazista", "Responder xingando a todos e que deveriam parar de perder tempo em discussões vagas", "A", f"{insert_newlines(feedback4)}"]
    ]

    return perguntas_alternativas_respostas[numero_da_pergunta]


#Perguntas e gabarito - ACABA

#SETUP DO JOGO - INICIA
pontos = 0

def inicio(): # Tela inicial da interface, que inicia a corrente de questões.
    global numeros_usados
    global pontos
    global numero_da_pergunta
    numeros_usados = []
    pontos = 0
    numero_da_pergunta = 0

    inicial0 = Label(window, text="Quiz", font=("Arial", 20))
    inicial0.grid(column=1, row=0, columnspan=2)

    inicial1 = Label(window, text="Avaliação de valores ético-morais aplicados.", font=("Arial", 18))
    inicial1.grid(column=1, row=1, columnspan=2)

    inicial2 = Label(window, text="Você é um agente secreto, passou por e executou já diversas missões na vida.\n Porém, na sua próxima missão, em virtude com as inteligências governamentais para a paz mundial,\n você precisa passar por um teste de Ética e Moral, e se encontra coagido,\n a modo que nunca havia questionado sua frieza.\n Suas respostas neste teste serão a CHAVE do seu FUTURO!", font=("Arial", 12))
    inicial2.grid(column=1, row=2, columnspan=2)

    inicial3 = Label(window, text="Escolha a alternativa que mais se encaixe para a situação", font=("Arial", 12))
    inicial3.grid(column=1, row=3, columnspan=2)
    
    #destroy_inicio() abre espaço para uma questão entrar no grid
    def destroy_inicio():
        inicial0.destroy()
        inicial1.destroy()
        inicial2.destroy()
        inicial3.destroy()
        iniciar.destroy()
        question(perguntas(aleatorio()))

    iniciar = Button(window, text="Iniciar", bg="lightgreen", command=destroy_inicio)
    iniciar.grid(column=1, row=4, columnspan=2)

numero_da_pergunta = 0

def question(y): # y deve ser uma lista neste formato: [pergunta, alternativa_A, alternativa_B, alternativa_C, alternativa_D, alternativa_E, alternativa_correta]
    global numero_da_pergunta
    numero_da_pergunta += 1 
    pergunta = Label(window, text=f"Q{numero_da_pergunta}: {y[0]}", font=("Arial", 12), justify=LEFT)
    pergunta.grid(column=1, row=0, columnspan=2)
    altA = Button(window, text=f"A. {y[1]}", width=120, command=lambda x = "A": conferir_gabarito(x))
    altA.grid(column=1, row=1, columnspan=2)
    altB = Button(window, text=f"B. {y[2]}", width=120, command=lambda x = "B": conferir_gabarito(x))
    altB.grid(column=1, row=2, columnspan=2)
    altC = Button(window, text=f"C. {y[3]}", width=120, command=lambda x = "C": conferir_gabarito(x))
    altC.grid(column=1, row=3, columnspan=2)
    altD = Button(window, text=f"D. {y[4]}", width=120, command=lambda x = "D": conferir_gabarito(x))
    altD.grid(column=1, row=4, columnspan=2)
    altE = Button(window, text=f"E. {y[5]}", width=120, command=lambda x = "E": conferir_gabarito(x))
    altE.grid(column=1, row=5, columnspan=2)

    def conferir_gabarito(x):
        global pontos
        if x.upper() == y[6]:
            print("Alternativa correta!")
            pontos += 1
            correto()
        else:
            print("Alternativa incorreta!")
            errado()

    def correto():
        pergunta.destroy()
        altA.destroy()
        altB.destroy()
        altC.destroy()
        altD.destroy()
        altE.destroy()
        congratulations = Label(window, text="Acertou!", fg="green", font=("Arial", 15))
        congratulations.grid(column=1, row=2, columnspan=2)

        prox = Button(window, text="Próxima questão", command=lambda numero_da_pergunta = numero_da_pergunta :next_question(numero_da_pergunta))
        prox.grid(column=1, row=4, columnspan=2)

        def next_question(numero_da_pergunta):
            congratulations.destroy()
            prox.destroy()
            if numero_da_pergunta < 10:
                question(perguntas(aleatorio()))
            else:
                pergunta.destroy()
                altA.destroy()
                altB.destroy()
                altC.destroy()
                altD.destroy()
                altE.destroy()
                def texto_de_despedida(acertos):
                    if acertos == 0 or acertos == 1 or acertos == 2:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste. Se você não escolheu errar propositalmente,\n então, francamente, repense sobre as pequenas ações e decisões que tem tomado durante a vida.\n Às vezes, pode apenas não ter a experiência, às vezes, você está impactando negativamente\n pessoas ao redor ou criando consequências piores para si. Claro, esse teste é informal,\n mas tem intuito de acender luzes. Relaxe, e tente consumir obras,\n como filmes, séries, documentários, vídeos ou livros que discutam questões sociais,\n que não é difícil de encontrar um que atenda ao seu gosto hoje em dia."  
                    if acertos == 3 or acertos == 4:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste,  apesar da pontuação baixa, \n não significa necessariamente que é uma pessoa deturpada,\n mas que tem muito a aprender ainda sobre o bom senso e o seu cultivo. "
                    if acertos == 5 or acertos == 6:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste, você possui um bom senso\n adequado e comum, mas pelo visto, você pode melhorar muito mais, a partir de mais\n experiências da vida mesmo, mantendo sempre o respeito e evitando conflitos de qualquer origem. "
                    if acertos == 7 or acertos == 8:
                        return f"Você acertou {acertos} questões.\n Parabéns ao dobro! Obrigado por oferecer seu tempo ao teste, você tem um calibre moral\n forte e de bom valor para a difusão desses mesmos valores, continue cultivando o bom senso,\n a manter o respeito e ser contra conflito desnecessário, conforme sua personalidade e maturidade psicológica."
                    if acertos == 9 or acertos == 10:
                        return f"Você acertou {acertos} questões.\n Parabéns ao triplo! Obrigado por oferecer seu tempo ao teste e, claro, por dar\n atenção aos testes! Apesar dos diferentes problemas que tiver em sua vida,\n lembre-se sempre do seu potencial por carregar valores e modos autênticos.\n Aproveite e difunda a boa vontade com quem conhecer e com quem você se importa!"

                fim = Label(window, text=f"{texto_de_despedida(pontos)}")
                fim.grid(column=0, row=0, rowspan=3)
                novamente = Button(window, text="Jogar novamente", bg="red", fg="white", command=lambda: [inicio(), destroy_acabar()])
                novamente.grid(column= 2, row=5)
                def destroy_acabar():
                    fim.destroy()
                    novamente.destroy()

    def errado():
        pergunta.destroy()
        altA.destroy()
        altB.destroy()
        altC.destroy()
        altD.destroy()
        altE.destroy()

        congratulations = Label(window, text="Errou!", fg="red", font=("Arial", 15))
        congratulations.grid(column=1, row=1, columnspan=2)

        resposta = Label(window, text=f"{y[7]}")
        resposta.grid(column=1, row=2, columnspan=2)

        prox = Button(window, text="Próxima questão", command=lambda numero_da_pergunta = numero_da_pergunta :[next_question(numero_da_pergunta), resposta.destroy()])
        prox.grid(column=1, row=4, columnspan=2)

        def next_question(numero_da_pergunta):
            congratulations.destroy()
            prox.destroy()
            if numero_da_pergunta < 10:
                question(perguntas(aleatorio()))
            else:
                pergunta.destroy()
                altA.destroy()
                altB.destroy()
                altC.destroy()
                altD.destroy()
                altE.destroy()
                
                def texto_de_despedida(acertos):
                    if acertos == 0 or acertos == 1 or acertos == 2:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste. Se você não escolheu errar propositalmente,\n então, francamente, repense sobre as pequenas ações e decisões que tem tomado durante a vida.\n Às vezes, pode apenas não ter a experiência, às vezes, você está impactando negativamente\n pessoas ao redor ou criando consequências piores para si. Claro, esse teste é informal,\n mas tem intuito de acender luzes. Relaxe, e tente consumir obras,\n como filmes, séries, documentários, vídeos ou livros que discutam questões sociais,\n que não é difícil de encontrar um que atenda ao seu gosto hoje em dia."  
                    if acertos == 3 or acertos == 4:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste,  apesar da pontuação baixa, \n não significa necessariamente que é uma pessoa deturpada,\n mas que tem muito a aprender ainda sobre o bom senso e o seu cultivo. "
                    if acertos == 5 or acertos == 6:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste, você possui um bom senso\n adequado e comum, mas pelo visto, você pode melhorar muito mais, a partir de mais\n experiências da vida mesmo, mantendo sempre o respeito e evitando conflitos de qualquer origem. "
                    if acertos == 7 or acertos == 8:
                        return f"Você acertou {acertos} questões.\n Parabéns! Obrigado por oferecer seu tempo ao teste, você tem um calibre moral\n forte e de bom valor para a difusão desses mesmos valores, continue cultivando o bom senso,\n a manter o respeito e ser contra conflito desnecessário, conforme sua personalidade e maturidade psicológica."
                    if acertos == 9 or acertos == 10:
                        return f"Você acertou {acertos} questões.\n Parabéns ao triplo! Obrigado por oferecer seu tempo ao teste e, claro, por dar\n atenção aos testes! Apesar dos diferentes problemas que tiver em sua vida,\n lembre-se sempre do seu potencial por carregar valores e modos autênticos.\n Aproveite e difunda a boa vontade com quem conhecer e com quem você se importa!" 

                fim = Label(window, text=f"{texto_de_despedida(pontos)}")
                fim.grid(column=0, row=0, rowspan=3)
                novamente = Button(window, text="Jogar novamente", bg="red", fg="white", command=lambda: [inicio(), destroy_acabar()])
                novamente.grid(column= 2, row=5)
                def destroy_acabar():
                    fim.destroy()
                    novamente.destroy()




inicio()




#SETUP DO JOGO - ACABA

#LOADING SUPER DESNECESSARIAMENTE LEGAL - INICIA
print("Loading this BEAUTIFUL GAME!")
loading = "Loading"

for z in range(0, 20, 1):
    loading = loading + "."
    time.sleep(0.1)
    print(loading)
    
print("Loading realizado com sucesso")
#LOADING SUPER DESNECESSARIAMENTE LEGAL - ACABA

#Mantém a janela aberta
mainloop()