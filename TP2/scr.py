
import re

def markdown_to_html(text):
    # Usado para o titulo
    # ^ ve o inicio da frase;
    # (#+) Este é um grupo de captura que procura uma sequência de um ou mais caracteres # consecutivos.
    # \s Qualquer caractere de espaço em branco
    # (.+) Outro grupo de captura que procura um ou mais caracteres de qualquer tipo (exceto quebras de linha).
    # $ Indica o final da linha.
    # O que faz é vai ate ao ultimo espaco branco e ve o que esta aseguir para ver se o fim
    # Ve varias vezes se existe este padrao com o flags=re.MULTILINE
    titulos = re.compile(r'^(#+)\s(.+)$', flags=re.MULTILINE)
    t = re.sub(titulos, r'<h1>\2</h1>', text)

    # Expressão regular para itálico
    # \* ve o que delimita o padrao procurado
    # (.+?) qualquer caractere um ou mais vezes (+), mas de forma não gananciosa(ou seja ve a primeir a instancia em a aparece o * no fim)
    italic = re.compile(r'\*(.+?)\*', flags=re.MULTILINE)
    i = re.sub(italic, r'<i>\1</i>', t)

    image = re.compile(r'!\[([^]]+)\]\(([^)]+)\s*\)')
    html_text = re.sub(image, lambda match: f'<img src="{match.group(2)}" alt="{match.group(1)}"/>', i)
    
    # \[ e \] Delimitadores de colchetes que marcam o início e o fim do texto do link.
    # ([^]]+) Grupo de captura que corresponde a qualquer sequência de caracteres que não seja ']', representando o texto do link.
    # \) Delimitador de parênteses que marca o início do URL do link.
    # ([^)]+) Grupo de captura que corresponde a qualquer sequência de caracteres que não seja ')', representando o URL do link.
    link = re.compile(r'\[([^]]+)\]\(([^)]+)\)')
    l = re.sub(link, r'<a href="\2">\1</a>', html_text)

    return l

def ordered_lists_check(html_text: str) -> str:
    lines = html_text.split('\n')
    result = []
    ol_open = False
    
    for line in lines:
        regex = r"^ {0,3}\d+\. (.+)$"
        match = re.match(regex, line)
        
        if match:
            content = match.group(1)
            if not ol_open:
                result.append("<ol>")
                ol_open = True
            result.append(f"<li>{content}</li>")
        else:
            if ol_open:
                result.append("</ol>")
                ol_open = False
            result.append(line)
    
    if ol_open:
        result.append("</ol>")
    
    return "\n".join(result)

# Exemplo
markdown_input = "# Exemplo\n\nComo se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...\nEste é um *exemplo jjjjjj* ...\n\n1. Primeiro item\n2. Segundo item\n3. Terceiro item\n\nComo pode ser consultado em [página da UC](http://www.uc.pt)\n"
html_output = markdown_to_html(markdown_input)
processed_html = ordered_lists_check(html_output)

print(processed_html)
