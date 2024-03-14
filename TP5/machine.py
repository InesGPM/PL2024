import json
import re

# Função para carregar o stock de produtos a partir de um arquivo JSON
def carregar_stock(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            stock = json.load(arquivo)
        return stock
    except FileNotFoundError:
        print("Arquivo de stock não encontrado. Criando novo stock.")
        return []
    
# Função para validar o formato do código do produto
def validar_codigo(codigo_produto):
    return re.match(r'[a-zA-Z]{1}\d{2}', codigo_produto)

def validar_quantidade(quant):
    return re.match(r'\d+', quant)

def validar_valor(valor):
    return re.match(r'\d+[EC](?:\s+\d+[EC])*', valor)


# Função para salvar o stock de produtos em um arquivo JSON
def salvar_stock(stock, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(stock, arquivo, indent=4)

# Função para listar os produtos no stock
def listar_produtos(stock):
    print("cod | nome | quantidade | preço")
    print("-" * 33)
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']//100}e {produto['preco']%100}c")

# Função para processar o comando de inserção de moeda
def processar_moeda(saldo_atual, moedas):
    saldo = saldo_atual
    for moeda in moedas:
        if moeda[len(moeda)-1]==("E"):
            saldo += int(moeda[:-1]) * 100
        elif moeda[len(moeda)-1]==("C"):
            saldo += int(moeda[:-1])
    return saldo

# Função para selecionar um produto
def selecionar_produto(stock, codigo_produto, saldo_atual):
    for produto in stock:
        if produto['cod'] == codigo_produto:
            if produto['quant'] > 0 and saldo_atual >= produto['preco']:
                produto['quant'] -= 1
                saldo_atual -= produto['preco']
                print(f"maq: Pode retirar o produto dispensado: {produto['nome']}")
                print(f"maq: Saldo = {saldo_atual//100}e {saldo_atual%100}c")
            elif produto['quant'] == 0:
                print("maq: Produto esgotado.")
            else:
                print(f"maq: Saldo insuficiente.\nmaq: Saldo = {saldo_atual//100}e {saldo_atual%100}c\nmaq: Preco de {produto['nome']}= {produto['preco']}c")
            return saldo_atual
    print("maq: Produto não encontrado.")
    return saldo_atual
import re


def restock_produto(stock, codigo_produto):
    if not validar_codigo(codigo_produto):
        print("maq: Código do produto inválido.")
        return
    
    for produto in stock:
        if produto['cod'] == codigo_produto:
            if produto['quant'] == 10:
                print("maq: O produto já atingiu a capacidade máxima. Por favor, utilize outro código.")
                return
            
            print(f"maq: Restock de {produto['nome']}")
            print(f"maq: Introduza a quantidade sem ultrapassar a capacidade de 10 uni (quantidade atual: {produto['quant']})")
            comando_quantidade = input(">> ").strip().upper()
            
            if not validar_quantidade(comando_quantidade):
                print("maq: Quantidade inválida. Por favor, insira apenas números.")
                return
            
            if int(comando_quantidade) + produto['quant'] > 10:
                print("maq: Ultrapassou a capacidade limite")
                return
            
            produto['quant'] += int(comando_quantidade)
            
            print("maq: Pretende alterar o preço do produto (Nao ou valor)")
            final = input(">> ").strip().upper()
            
            if final == "NAO":
                print("maq: Restock completo")
                return
            else:
                if not validar_valor(final):
                    print("maq: Valor inválido. Use o formato correto, por exemplo: 10e, 30c, 10c, 30e")
                    return
                
                produto['preco'] = processar_moeda(0, final.split())
                print(f"maq: Restock completo e valor alterado para {produto['preco']}")
                return
    
    print("maq: Restock de um novo produto")
    print("maq: Introduza o nome")
    nome = input(">> ").strip()
    print("maq: Introduza a quantidade (max 10)")
    quantidade = input(">> ").strip().upper()
    
    if not validar_quantidade(quantidade):
        print("maq: Quantidade inválida. Por favor, insira apenas números.")
        return
    
    quantidade = int(quantidade)
    
    if quantidade > 10:
        print("maq: Quantidade ultrapassou a capacidade limite (max 10)")
        return
    
    print("maq: Introduza o preço")
    preco = input(">> ").strip().upper()
    
    if not validar_valor(preco):
        print("maq: Valor inválido. Use o formato correto, por exemplo: 10e, 30c, 10c, 30e")
        return
    
    preco = processar_moeda(0, preco.split())

    novo_produto = {
        'cod': codigo_produto,
        'nome': nome,
        'quant': quantidade,
        'preco': preco
    }
    
    stock.append(novo_produto)
    print("maq: Novo produto adicionado ao estoque")


# Função principal
def main():
    arquivo_stock = 'stock.json'
    stock = carregar_stock(arquivo_stock)
    saldo = 0

    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        comando = input(">> ").strip().upper()
        if comando == 'LISTAR':
            listar_produtos(stock)
        elif comando.startswith('MOEDA'):
            moedas = comando.split()[1:]
            print(moedas)
            saldo = processar_moeda(saldo, moedas)
            print(f"maq: Saldo = {saldo//100}e {saldo%100}c")
        elif comando.startswith('SELECIONAR'):
            codigo_produto = comando.split()[1]
            saldo = selecionar_produto(stock, codigo_produto, saldo)
        elif comando.startswith('RESTOCK'):
            codigo_produto = comando.split()[1]
            restock_produto(stock, codigo_produto)
        elif comando == 'SAIR':
            troco = saldo
            print(f"maq: Pode retirar o troco: {troco//100}e {troco%100}c.")
            print("maq: Até à próxima")
            salvar_stock(stock, arquivo_stock)
            break
        else:
            print("maq: Comando inválido.")

if __name__ == "__main__":
    main()
