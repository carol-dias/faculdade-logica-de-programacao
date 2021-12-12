from random import sample #Importa o método sample da biblioteca random

inscritos = {} #Cria dicionário para inscritos
ARQUIVO_INSCRITOS = 'inscritos.pkl' #Onde serão armazenadas as informações dos inscritos

#Função que carrega o arquivo do módulo pickle
def carrega_arquivo_pkl():
    import pickle
    import os
    global inscritos
    if not os.path.exists(ARQUIVO_INSCRITOS):
        grava_arquivo_pkl() #Se não houver arquivo existente, chama a função que grava o arquivo
    arquivo_inscritos = open(ARQUIVO_INSCRITOS, 'rb')
    inscritos = pickle.load(arquivo_inscritos)

#Função que grava o arquivo do módulo pickle
def grava_arquivo_pkl():
    import pickle #Importa o módulo pickle
    arquivo_inscritos = open(ARQUIVO_INSCRITOS, 'wb')
    pickle.dump(inscritos, arquivo_inscritos)

#Função que carrega o arquivo do módulo pickle
def carrega_arquivo():
    import os
    if not os.path.exists(ARQUIVO_INSCRITOS):
        grava_arquivo()
    else:
        arquivo = open(ARQUIVO_INSCRITOS, 'r')
        linhas = []
        for linha in arquivo:
            linhas.append(linha.strip())
        print(linhas)
        for linha in linhas:
            inscrito = {}
            dados_inscrito = linha.split(";")
            voucher = dados_inscrito[0]
            inscrito['nome'] = dados_inscrito[1]
            inscrito['email'] = dados_inscrito[2]
            inscrito['telefone'] = dados_inscrito[3]
            inscrito['curso'] = dados_inscrito[4]
            inscritos[voucher] = inscrito
        arquivo.close()

#Função que grava o arquivo
def grava_arquivo():
    with open(ARQUIVO_INSCRITOS, 'w') as arquivo:
        for voucher, inscrito in inscritos.items():
            arquivo.write(str(voucher)+";"+inscrito['nome']+";"+inscrito['email']+";"+inscrito['telefone']+";"+inscrito['curso']+'\n')
        arquivo.close()

#Função que executa o menu principal do programa
def menu():
    print('*'*10 + 'Menu' + '*'*10)
    return input('1 - Nova inscrição \n2 - Visualizar inscrição \n0 - Encerrar \nOpção escolhida: ')

#Função que permite a inscrição do candidato ao(s) curso(s)
def inscricao():  
    um_inscrito = {}
    voucher_inscrito = sample(range(1, 400), 1)
    print('Voucher: ', voucher_inscrito)
    um_inscrito['nome'] = input('Nome: ')
    um_inscrito['email'] = input('E-mail: ')
    um_inscrito['telefone'] = int(input('Telefone: '))
    um_inscrito['curso'] = input('Curso: ')
    
def lista(): #Função que permite listar os inscritos
    inscritos_por_nome = {}  

    for voucher, inscrito in inscritos.items():  #Loop responsável por criar um dicionário em que o nome do inscrito é a chave e o voucher é o valor
        nome = inscrito['nome']
        inscritos_por_nome[nome] = voucher

    nomes_ordenados = sorted(inscritos_por_nome.keys())  #Retorna uma lista ordenada dos nomes dos inscritos

    for nome_inscrito in nomes_ordenados:  #Loop que percorre a lista dos inscritos e apresenta as informações
        voucher = inscritos_por_nome[nome_inscrito]
        print('*'*10)
        print('Voucher: ', voucher)
        print('Nome: ', inscrito['nome'])
        print('E-mail: ', inscrito['email'])
        print('Telefone: ', inscrito['telefone'])
        print('Curso', inscrito['curso'])
    print("*"*10)

def main():
    carrega_arquivo_pkl()
    while True:
        opcao = menu()
        if opcao == '1': #Nova inscrição
            inscricao()
        elif opcao == '2':  #Visualizar inscrição
            lista()
        elif opcao == '0':  #Encerrar
            print('Programa encerrado.')
            grava_arquivo_pkl()
            break
        else:
            print('Erro. Digite uma opção válida!') 


if __name__ == '__main__':
    main()