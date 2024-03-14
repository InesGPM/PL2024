import re

# Definição dos tokens e suas expressões regulares
tokens = [
    ('SELECT', r'SELECT'),               # Token para a palavra-chave 'SELECT'
    ('FROM', r'FROM'),                   # Token para a palavra-chave 'FROM'
    ('WHERE', r'WHERE'),                 # Token para a palavra-chave 'WHERE'
    ('ID', r'[a-zA-Z]+'),                # Token para identificadores de colunas ou tabelas formados por 1 ou mais letras
    ('COMMA', r','),                     # Token para vírgula
    ('NUMBER', r'\d+'),                  # Token para números inteiros (\d) aparecendo 1 ou mais vezes (+)
    ('GREATER_EQUAL', r'>='),            # Token para o operador de maior ou igual
    ('OPERATOR', r'[>=<]'),              # Token para operadores de comparação (>, <)
    ('NEWLINE', r'\n'),                  # Token para nova linha (\n)
    ('SPACE', r'\s+'),                   # Token para espaços em branco
    ('ERROR', r'.')                      # Token para qualquer outro caractere (erro)
]


def lex(input_string):
    
    tokens_regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)
    token_regex = re.compile(tokens_regex)
    pos = 0

    while pos < len(input_string):
        match = token_regex.match(input_string, pos) # Encontrar a próxima correspondência
        if match:
            group_name = match.lastgroup
            value = match.group(group_name) # Obter o nome do grupo e o valor correspondente
            if group_name != 'SPACE': # Ignorar espaços em branco
                yield group_name, value
            pos = match.end()# Atualizar a posição
        else:
            raise SyntaxError('Erro')
            break

query = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"
for token in lex(query):
    print(token)
