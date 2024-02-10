from collections import defaultdict
import os

# Nome do arquivo CSV
nome_do_arquivo = "emd.csv"

#verifica se o arquivo existe
def existe_arquivo(nome_arquivo):
    return os.path.exists(nome_arquivo)

# Lista com todas as informações
infs = list()

# Lê o ficheiro e guarda as informações
def read_csv(reader: str): 
    reader = open(reader, 'r') #abre o csv para ler as inf

    for line in reader:
        # Divide a linha em uma lista usando a vírgula como delimitador
        values = line.strip().split(',')
        
        # Adiciona a lista à lista infs
        if values[0] != '_id':
            infs.append(values)

    return infs #Uma lista de listas, onde cada lista representa uma linha do arquivo CSV.


# Ordenando a lista com base na modalidade desportiva (nono elemento)
def ordenar_por_modalidade(infs):
    return sorted(infs, key=lambda x: x[8])

# Calcula a porcentagem de atletas aptos
def percent_aptos(infs):
    l = 0
    contaAptos=0
    while l < len(infs):
        # Pega na lista da infs usando o índice l
        linha = infs[l]

        # Verifica se o ultimo elemento da linha é igual a "true" ou seja esta apto
        if linha[12].lower() == "true":
            # Realize as operações desejadas com a linha
            contaAptos+=1

        # Incrementa o valor de l
        l += 1
    
    return round((contaAptos*100)/l,2)


def distribuicao_por_escalao(infs):
    # defaultdict(int) cria um dicionário onde os valores associados a cada chave sao inteiros.
    escaloes = defaultdict(int)# Dicionário para armazenar atletas por escalão etário.
    
    for linha in infs:
        idade = int(linha[5])
        escalao = (idade // 5) * 5  # Calcula o escalão arredondando para baixo em intervalos de 5 anos
        escaloes[escalao] += 1
    
    return escaloes

# Chama a função para ler o arquivo verificando se ele existe
if existe_arquivo(nome_do_arquivo):
    imprimir= read_csv('emd.csv')
    # Imprime a lista base
    #print(imprimir) 

    # Imprime a lista ordenada por modalidade
    print("Lista ordenada alfabeticamente das modalidades desportivas\n", ordenar_por_modalidade(imprimir)) 

    #Imprime a percentagem de atletas aptos e nao aptos
    print("Aptos:", percent_aptos(imprimir), "\nNão Aptos:" , (100 - percent_aptos(imprimir)))
    
    # Imprime a distribuição por escalão etário
    print("Distribuição por escalão etário:")
    for escalao, quantidade in distribuicao_por_escalao(imprimir).items():
        print(f"{escalao}-{escalao+4}: {quantidade} atletas")


