#Programa que troca as vogais do nome por caracteres especiais

#Dados de entrada
nome = (input('Insira um nome: '))

#Deixa todas as letras em caixa alta
nome_maiusc = nome.upper()

#Primeira saída - nome em caixa alta
print(nome_maiusc)

#Segunda saída - utiliza o método replace para a troca de caracteres na string
print(nome_maiusc.replace('A','@').replace('E','&').replace('I','!').replace('O','#').replace('U','*'))