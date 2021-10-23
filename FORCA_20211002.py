# ----------------------------------------------------------------------------------------------------------------------
# PROJETO 01 - JOGO DA FORCA
# Santander Coders - Let's Code
# Autoras: Bruna Lima, Carolina Coutinho e Izadora Bittencourt 
# ----------------------------------------------------------------------------------------------------------------------


#Importando bibliotecas
import unidecode                                   #biblioteca para diferenciar os acentos      
import random                                      #módulo random p/ a função selecionarAleatorio
import turtle                                      #módulo turtle p/ o desenho da forca

# ----------------------------------------------------------------------------------------------------------------------

def carregarArquivo ():
    '''
    Função que pede a categoria ao usuário, carrega o arquivo .txt correspondente e retorna a lista de palavras.
    '''

    nomesCategorias = {"1": "Frutas e Verduras",
    "2": "Animais",
    "3": "Verbos",
    "4": "Países",
    "5": "Esportes"
    }
    categoria = input("\nCATEGORIAS\n1- Frutas e Verduras\n2- Animais\n3- Verbos\n4- Países\n5- Esportes\nQual categoria você deseja jogar? (1/2/3/4/5) ").strip()
    #while categoria != "1" and categoria != "2":
    while categoria not in ["1","2","3","4","5"]:
        print("Opção inválida!")
        categoria = input("Qual categoria você deseja jogar? (1/2/3/4/5) ").strip()
    print(f"Certo! Jogada na categoria {nomesCategorias[categoria]}.")

    categoriasArquivos = {"1": "Forca_frutasverduras.txt",
    "2": "Forca_animais.txt",
    "3": "Forca_verbos.txt",
    "4": "Forca_paises.txt",
    "5": "Forca_esportes.txt"
    }
    arquivo = open(categoriasArquivos[categoria], "r", encoding="utf-8")    #abre a nossa lista de palavras temática no modo leitura
    lista = arquivo.read()
    palavras = lista.split('\n')                                            #cria uma lista com as palavras
    return (palavras)
    arquivo.close()

def selecionarAleatoria(listaPalavras):
    '''
    Escolha da palavra aleatória de uma lista e retorna em caixa alta 
    '''
    escolha = ""
    while len(escolha) < 4:                     #filtrando as palavras da lista
        escolha = random.choice(listaPalavras)
    return escolha.upper()                      


def formatacao(palpite:str):
    '''
    Função que formata o palpite (retira acentos, espaços excedentes e coloca em caixa alta).
    '''
    return unidecode.unidecode(palpite.strip().upper())  


def palpiteLetra(letrasUsadas:list):
    '''
    Função responsável por pedir, validar e retornar uma letra palpite.
    '''

    palpite = formatacao(input("Digite uma letra: "))

    while palpite.isalpha() == False or len(palpite) != 1:
        print("Caracter(es) inválido(s).")
        palpite = formatacao(input("Entre com uma letra do alfabeto: "))

    while palpite in letrasUsadas:
        print("Você já utilizou essa letra.")
        palpite = formatacao(input("Tente outra: "))
        while palpite.isalpha() == False or len(palpite) != 1:
            print("Caracter(es) inválido(s).")
            palpite = formatacao(input("Entre com uma letra do alfabeto: "))
        #Dentro pois se não estivesse e o usuário digitasse alguma que já está na lista, e tentasse novamente com caracteres inválidos o programa aceitaria.

    return (palpite)


def palpiteMisto(listaImpressao:list, letrasUsadas:list):
    '''
    Função responsável por pedir, validar e retornar um palpite, seja ele palavra ou letra.
    Retorna também se o palpite é palavra ou letra.
    '''

    contPreenchidas = 0                    # Quantas letras foram preenchidas na palavra secreta
    contTotal = 0                          # Comprimento total da palavra sem considerar espaço e hífen
    for elemento in listaImpressao:
        if elemento != "_" and elemento != " " and elemento != "-":
            contPreenchidas += 1

        if elemento != " " and elemento != "-":
            contTotal += 1

    resp = "N"
    
    if contPreenchidas >= contTotal * 0.6 and contPreenchidas != contTotal - 1:
        resp = input("Gostaria de adivinhar a palavra? (S - SIM | N - NÃO) ").upper().strip()
        while resp != "S" and resp != "N":
            print("Resposta inválida!")
            resp = input("Gostaria de adivinhar a palavra? (S - SIM | N - NÃO) ").upper().strip()

    if resp == "S" or contPreenchidas == contTotal - 1:
        ehPalavra = True

        palpite = formatacao(input("Qual seu palpite da palavra? "))
        while len(palpite) != len(listaImpressao):
            print("Entrada inválida! Tamanho não corresponde ao da palavra secreta.")
            palpite = formatacao(input("Qual seu palpite da palavra? "))

    else:
        ehPalavra = False

        palpite = palpiteLetra(letrasUsadas)

    return (palpite, ehPalavra)


def checaPalpiteLetra(listaImpressao,erros,palavraSecreta,palpite):
    '''
    Função que checa a letra palpite, informa ao usuário e retorna a lista de impressão e a lista de erros
    atualizadas e também se o usuário errou.
    '''

    if palpite not in (unidecode.unidecode(palavraSecreta)):
            erros.append(palpite)
            errou=True
            print('Oops! A palavra não possui essa letra.')
            print("______________________________________")
          
    else:
        errou= False
        for index,letra in enumerate(unidecode.unidecode(palavraSecreta)):
            if letra == palpite:
                listaImpressao[index]=palavraSecreta[index]
        print('Boa! Você está no caminho certo.')
        print("______________________________________")
    return (listaImpressao,erros,errou)
    
def desenhaForca():
    t.up()
    t.goto(-80,-80)
    t.down()
    t.forward(150)
    t.right(180)
    t.forward(75)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(20)
    return

def desenhaCabeca():
    t.right(90)
    t.circle(30)    #cabeça, raio 30
    t.right(90)
    return

def desenhaCorpo():
    t.up()
    t.left(180)
    t.forward(60)
    t.down()
    t.forward(75)   #corpinho
    return

def desenhaPerna1():
    t.right(40)
    t.forward(40)   #perna direita
    t.up()
    return

def desenhaPerna2():
    t.right(180)
    t.forward(40)   #perna esquerda
    t.right(100)    
    t.down()
    t.forward(40)
    return

def desenhaBraco1():
    t.up()
    t.right(180)
    t.forward(40)
    t.right(40)
    t.forward(65) 
    t.right(140)
    t.down()
    t.forward(40)

def desenhaBraco2(): 
    t.right(180)
    t.forward(40)
    t.left(100)
    t.forward(40)

def desenhaRosto():
    t.up()
    t.right(180)
    t.forward(40)
    t.goto(145.00,70.00)    #coordenadas para o centro do circulo
    t.goto(135,80)          #olho esquerdo
    t.down()
    t.dot(10)
    t.up()
    t.goto(155,80)
    t.down()
    t.dot(10)
    t.up()
    t.goto(155,55)          #começo da boca
    t.setheading(120)       #seta o ângulo de abertura do traço
    t.down()
    t.circle(15, 120)       #faz um semi circulo de 120º e tamanho 15

def desenhaVitoria():
    t.reset()
    t.color('orange', 'yellow')
    t.speed(9)
    t.begin_fill()
    t.circle(130)            #o circulo será desenhado preenchido
    t.end_fill()
    t.color('black')
    t.up()
    t.goto(-35,145)           #coordenadas do olho esquerdo
    t.down()
    t.dot(25)
    t.up()
    t.goto(35,145)            #coordenadas do olho esquerdo
    t.down()
    t.dot(25)
    t.up()
    t.goto(-60,80)
    t.down()
    t.setheading(-60)
    t.circle(70, 120)

def desenhaDerrota():
    t.reset()
    t.color('orange', 'red')
    t.speed(9)
    t.begin_fill()
    t.circle(130)            #o circulo será desenhado preenchido
    t.end_fill()
    t.color('black')
    t.up()
    t.goto(-35,145)           #coordenadas do olho esquerdo
    t.down()
    t.dot(25)
    t.up()
    t.goto(35,145)            #coordenadas do olho esquerdo
    t.down()
    t.dot(25)
    t.up()
    t.goto(60,65)
    t.down()
    t.setheading(120)
    t.circle(70, 120)

def desenho (erros):
    if len(erros)==1:
        desenhaCabeca()
    elif len(erros)==2:
        desenhaCorpo()
    elif len(erros)==3:
        desenhaPerna1()
    elif len(erros)==4:
        desenhaPerna2()
    elif len(erros)==5:
        desenhaBraco1()
    elif len(erros)==6:
        desenhaBraco2()
    elif len(erros)==7:
        desenhaRosto()

def ganhouJogo(palavraSecreta):
    desenhaVitoria()
    print(f'\nEba! Você acertou a palavra secreta {palavraSecreta.capitalize()}!!!\nParabéns!! Você conseguiu salvar a vida do Brian!')
    jogarNovamente = input('Deseja jogar novamente? (S - SIM | N - NÃO) ').upper().strip()
    while jogarNovamente != "S" and jogarNovamente != "N":
        print("Resposta inválida!")
        jogarNovamente = input('Deseja jogar novamente? (S - SIM | N - NÃO) ').upper().strip()
    return (jogarNovamente)

def perdeuJogo(palavraSecreta):
    desenhaDerrota()
    print(f'\nPoxa! A palavra secreta era {palavraSecreta.capitalize()}.\nNão foi dessa vez que você salvou o Brian... :(') 
    jogarNovamente = input('Deseja jogar novamente? (S - SIM | N - NÃO) ').upper().strip()
    while jogarNovamente != "S" and jogarNovamente != "N":
        print("Resposta inválida!")
        jogarNovamente = input('Deseja jogar novamente? (S - SIM | N - NÃO) ').upper().strip()
    return (jogarNovamente)

def impressaoHistorico(vitorias:int, derrotas:int):
    '''
    Função que imprime o histórico de vitórias e derrotas de maneira personalizada.
    '''

    if vitorias == 0:
        textoVitoria = ""
    elif vitorias == 1: 
        textoVitoria = "1 vitória"
    else:
        textoVitoria = str(vitorias) + " vitórias"
    
    if derrotas == 0:
        textoDerrota = ""
    elif derrotas == 1: 
        textoDerrota = "1 derrota"
    else:
        textoDerrota = str(derrotas) + " derrotas"
        
    if textoVitoria != "" and textoDerrota != "":
        print(f'Você acumulou {textoVitoria} e {textoDerrota}.')
    elif textoVitoria != "":
        print(f'Você acumulou {textoVitoria}.')
    else:
        print(f'Você acumulou {textoDerrota}.')

def imprimirCabecalho():
    print(f'{"JOGO DA FORCA":*^60}\n')
    print(f'{" _____________________________________________________________________":^60}')
    print(f'{"|                              REGRAS                                 |":^60}')
    print(f'{"|                                                                     |":^60}')
    print(f'{"|> A palavra secreta inicialmente deve ser adivinhada letra por letra.|":^60}')
    print(f'{"|> Acumulando 7 palpites errados, o Brian é enforcado!                |":^60}')
    print(f'{"|> Faltando pelo menos 40% da palavra, você poderá inserir uma letra  |":^60}')
    print(f'{"|  ou tentar adivinhar a palavra inteira. Mas, cuidado! Se você optar |":^60}')
    print(f'{"|  pela palavra, você só terá uma chance! Se você não acertar a       |":^60}')
    print(f'{"|  palavra, o Brian será enforcado!                                   |":^60}')
    print(f'{"|> Você não precisa se preocupar com acentuações nos seus palpites.   |":^60}')
    print(f'{"|> Dica: para uma melhor visualização, divida sua tela em duas.       |":^60}')    
    print(f'{" _____________________________________________________________________":^60}')


def inicioJogo():
    listaPalavras = carregarArquivo()                          #chamada função de carregar o arquivo .txt
    palavraSecreta = selecionarAleatoria(listaPalavras)        #chamada função de escolher palavra aleatória
    
    #Mostrar a palavra com _ _ _ e o desenho inicial
    listaImpressao = ["-" if caracter == "-" else " " if caracter == " " else "_" for caracter in palavraSecreta]

    print (palavraSecreta)        #APAGAR! LINHA SOMENTE PARA TESTES 
   
    print ("\nPalavra secreta:", *listaImpressao)
    desenhaForca()
    

    letrasUsadas = []                          #Letras já inseridas (erros e acertos)
    erros = []                                 #Letras já inseridas (só erros)

    while len(erros)<7:
        palpite, ehPalavra = palpiteMisto(listaImpressao, letrasUsadas)
        if ehPalavra:            
            if palpite == unidecode.unidecode(palavraSecreta):
                return ganhouJogo(palavraSecreta), True #Retornando a resposta do usuário de jogar novamente e se ganhou

            else:
                return perdeuJogo(palavraSecreta), False #Retornando a resposta do usuário de jogar novamente e se ganhou
        
        else:
            letrasUsadas.append(palpite)
            listaImpressao,erros,errou = checaPalpiteLetra(listaImpressao,erros,palavraSecreta,palpite)
            if errou:
                desenho(erros)
            if len(erros) < 7:
                print("Letras já usadas:", *letrasUsadas)
                print("Quantidade de erros:", len(erros))
                print("\nPalavra secreta:\n", *listaImpressao,"\n")
            else:
                print("Quantidade de erros:", len(erros))

            if "_" not in listaImpressao:
                return ganhouJogo(palavraSecreta), True #Retornando a resposta do usuário de jogar novamente e se ganhou
    else:
        return perdeuJogo(palavraSecreta), False #Retornando a resposta do usuário de jogar novamente e se ganhou


#CÓDIGO PRINCIPAL        

# Funções para inicializar o desenho
s = turtle.Screen()
t = turtle.Pen()

imprimirCabecalho()

jogarNovamente = "S"

vitorias = 0
derrotas = 0
while jogarNovamente == 'S':
    t.reset()
    jogarNovamente, vitoria = inicioJogo()
    if vitoria:
        vitorias += 1
    else:
        derrotas += 1


print("\nObrigada por jogar com a gente!")
impressaoHistorico(vitorias, derrotas)
print("Até a próxima!")

            