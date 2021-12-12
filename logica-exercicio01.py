# Programa que verifica o nível do ensino de acordo com a idade

while True: 
    #Dados de entrada 
    nome = input('Insira o nome: ')
    idade = int(input('Insira a idade: ')) #Define que só pode receber valor inteiro

    #Atribui à variável ensino uma string de acordo com a idade informada
    if idade >= 15:
        ensino = 'no Ensino Médio'
    elif idade >= 11:
        ensino = 'no Ensino Fundamental II'
    elif idade >= 6:
        ensino = 'no Ensino Fundamental I'
    elif idade >= 1:
        ensino = 'na Educação Infantil'
    else:
        ensino = 'em idade não-escolar'

    #Concatenação de strings que formam a saída apresentada ao usuário
    print('A(o) aluna(o) ' + nome + ' tem ' + str(idade) + ' ano(s) e está ' + ensino) 

    #Verifica se o programa deve continuar
    encerra = int(input('Deseja continuar?    0 - Não    1 - Sim \n')) #Define que só pode receber valor inteiro

    if encerra == 1: #Se o input for 1, continua o loop
        continue
    elif encerra == 0: #Se o input for 0, finaliza o loop
        print('Programa encerrado.')
        break
    else: #Se o input não for um dos valores solicitados, continua o loop
        print('Resposta inválida. O programa continuará em funcionamento.')