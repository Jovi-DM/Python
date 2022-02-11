import pandas as pd
import csv

T_linhas = 0
aux = 0
indice = 0

arq = open('archive.txt', 'r') #Put the name of txt file into 'archive.txt' content the numbers that you want to find
# Número total de linhas no txt
for linha in arq:
    T_linhas += 1

print("Numero de linhas no arquivo: ", T_linhas) #Used to know how many lines you have in txt file
arq.close()

manipulador = open('archive.txt', 'r') #Put the name of txt file into 'archive.txt' content the numbers that you want to find
linhas = manipulador.readlines()

print(linhas)
# Remoção de todos os caracteres /n
# Removing all caracteres '/n' from txt file
linhas = list(map(lambda s: s.strip(), linhas))

# Print para verificar se foram removidos os /n de cada elemento da lista
# Print to check if all the caracteres '/n' was removed from txt archive
print(linhas)

# Gerar arquivo final já editado
# Gonna create a new archive csv the end file
f = open('newfile.csv', 'w', newline='') # Put into 'newfile.csv' the name of end file gonna be created
w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter='~')

# Abrir arquivo csv principal
# Open the main csv file which you will use to look up the txt information
with open('Teste.csv') as arquivo_etiquetas: #Put into 'Teste.csv' the main csv
    tabela = csv.reader(arquivo_etiquetas, delimiter=';')

    for l in tabela:
        unidade = l[0]
        status = l[1]
        tombos = l[2]
        lotacao = l[3]
        descricao = l[4]

        # Verifica se leu e comparou todo o txt
        # Check if the program readed and compare all the txt file
        while (indice < T_linhas):
            # Se achar alguma igual, altera o status
            # If find a match, change the status
            if linhas[indice] == tombos:
                status = "Alterado"
            indice += 1
        indice = 0
        w.writerow([unidade, status, tombos, lotacao, descricao])

f.close()

manipulador.close()
