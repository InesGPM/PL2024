import re

def processar_texto(somador, texto):
    numeros = [int(numero) for numero in re.findall(r'\d+', texto)] #encontra no texto todos os numeros e poem os numa lista

    # Atualizar soma se necessário, apenas se o somador estiver ligado
    if somador[0] :
        somador = (somador[0], somador[1] + sum(numeros)) #somador[0] = ligado/desligado e somador[1]= soma

    # Verificar ligar ou desligar com base no texto
    if "off" in texto.lower():
        somador = (False, somador[1])
    elif "on" in texto.lower():
        somador = (True, somador[1]) 

    # Atualizar resultado com base na presença do comando de igual
    resultado = somador[1] if "=" in texto else None

    # Reiniciar a soma se o resultado não for None
    if resultado is not None and "off" not in texto.lower():
        somador = (somador[0], 0)

    return resultado, somador #resultado da soma e novo estado 

# Exemplo de uso
somador = (True, 0) #(ligado/desligado, soma atual)

# Texto de exemplo
texto_exemplo = """
On1NVDKJ234jpoiaJIOfçjbfçbjçi56=Off
7VNKSLD89
JVKNDSVKJOn
10NKLVNS1
20JIOSJDEFOJIO=Off
JJJ30kcnvlosnvio
"""



comandos = re.split(r'(on|off|-?[0-9]+|=)', texto_exemplo)

# Processar cada comando individualmente
for comando in comandos:
    resultado, somador = processar_texto(somador, comando)
    if resultado is not None:
        print(f"Resultado: {resultado}, Estado do Somador: {somador}")
