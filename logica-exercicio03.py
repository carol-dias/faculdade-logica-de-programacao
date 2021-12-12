import numpy as np #Importa biblioteca que trabalha com vetores e matrizes

def primeira_fase(): #Função que executa a primeira fase do jogo
    primeira_matriz = np.array([['*', '*', '_', 'G'], ['R', '_', '*', '*']]) #Cria matriz da fase 1 com biblioteca NumPy
    print('\nBem vindos à fase 1! \nNa fase 1, o jogador deve alocar RATO e GATO na seguinte matriz que representa os quartos:')
    print(primeira_matriz) #Apresenta a matriz ao jogador

    #Dados de entrada
    gato = int(input('Em qual posição deseja colocar o GATO?  '))
    rato = int(input('Em qual posição deseja colocar o RATO?  '))
    
    if gato == 3 and rato == 6: 
        segunda_fase() #Se o jogador acertar as posições, chama a função que executa a segunda fase do jogo
    else:
        print('\nQue pena, você perdeu :(') #Se o jogador errar as posições, encerra o jogo

def segunda_fase(): #Função que executa a segunda fase do jogo
    segunda_matriz = np.array([['_', '*', '*', '*'], ['*', 'C', '_', '_']]) #Cria matriz da fase 2 com biblioteca NumPy
    print('\nBem vindos à fase 2! \nNa fase 2, o jogador deve alocar CÃO, CÃO e OSSO na seguinte matriz que representa os quartos:')
    print(segunda_matriz) #Apresenta a matriz ao jogador

    #Dados de entrada
    cao1 = int(input('Em qual posição deseja colocar o primeiro CÃO?  '))
    cao2 = int(input('Em qual posição deseja colocar o segundo CÃO?  '))
    osso = int(input('Em qual posição deseja colocar o OSSO?  '))
    
    if (cao1 == 7 or cao1 == 8) and (cao2 == 7 or cao2 == 8) and osso == 1:
        terceira_fase() #Se o jogador acertar as posições, chama a função que executa a terceira fase do jogo
    else:
        print('\nQue pena, você perdeu :(') #Se o jogador errar as posições, encerra o jogo

def terceira_fase(): #Função que executa a terceira fase do jogo
    terceira_matriz = np.array([['_', '*', '*', '*'], ['_', 'G', '_', '*']]) #Cria matriz da fase 3 com biblioteca NumPy
    print('\nBem vindos à fase 3! \nNa fase 3, o jogador deve alocar GATO, OSSO e RATO na seguinte matriz que representa os quartos:')
    print(terceira_matriz) #Apresenta a matriz ao jogador

    #Dados de entrada
    gato = int(input('Em qual posição deseja colocar o GATO?  '))
    osso = int(input('Em qual posição deseja colocar o OSSO?  '))
    rato = int(input('Em qual posição deseja colocar o RATO?  '))

    if gato == 7 and osso == 5 and rato == 1:
        quarta_fase() #Se o jogador acertar as posições, chama a função que executa a quarta fase do jogo
    else:
        print('\nQue pena, você perdeu :(') #Se o jogador errar as posições, encerra o jogo

def quarta_fase(): #Função que executa a quarta e última fase do jogo
    quarta_matriz = np.array([['_', '_', '_', '*'], ['*', 'R', '*', '*']]) #Cria matriz da fase 4 com biblioteca NumPy
    print('\nBem vindos à fase 4! \nNa fase 4, o jogador deve alocar OSSO, QUEIJO e QUEIJO na seguinte matriz que representa os quartos:')
    print(quarta_matriz) #Apresenta a matriz ao jogador

    #Dados de entrada
    osso = int(input('Em qual posição deseja colocar o OSSO?  '))
    queijo1 = int(input('Em qual posição deseja colocar o primeiro QUEIJO?  '))
    queijo2 = int(input('Em qual posição deseja colocar o segundo QUEIJO?  '))

    if osso == 2 and (queijo1 == 1 or queijo1 == 3) and (queijo2 == 1 or queijo2 == 3):
        print('\nParabéns, você ganhou!') #Se o jogador acertar as posições, torna-se vitorioso - encerra o jogo
    else:
        print('\nQue pena, você perdeu :(') #Se o jogador errar as posições, encerra o jogo
    

print('***** Jogo HOTEL DOS ANIMAIS ***** \n\nEspecificando posição:') #Cabeçalho do jogo

posicao = np.array([[1, 2, 3, 4], [5 , 6, 7, 8]]) #Cria matriz das posições do jogo com biblioteca NumPy
print(posicao) #Mostra o valor referente a cada campo da matriz

primeira_fase() #Chama a função que executa a primeira fase do jogo - aberta a todos os jogadores





