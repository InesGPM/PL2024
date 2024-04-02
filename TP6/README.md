# Trabalho 6 

## Requerimento:
Garantir que as regras de produção sejam LL(1) e determinar a prioridade dos operadores, além de calcular os LookAhead para todas as regras de produção.

__Exemplo da linguagem:__ <br>
  ?a  <br>
  b=a*2/(27-3)  <br>
  !a+b  <br>
  c=a*b/(a/b)


# Gramática para Linguagem de Programação Simples.

## Terminais:
- `id`: Identificador
- `num`: Número
- `?`: Operador de leitura
- `!`: Operador de impressão
- `=`: Operador de atribuição
- `+`, `-`: Operadores de adição e subtração
- `*`, `/`: Operadores de multiplicação e divisão
- `(`, `)`: Parênteses

## Não-Terminais:
- `S`: Início do programa
- `LER`: Regra de leitura
- `IMP`: Regra de impressão
- `ATRIB`: Regra de atribuição
- `EXP`: Expressão aritmética
- `TERM`: Termo na expressão
- `FATOR`: Fator na expressão

## Produções:

- S -> LER | IMP | ATRIB
- LER -> '?' id
- IMP -> '!' EXP
- ATRIB -> id '=' EXP
- EXP -> TERM RESTO_EXP
- RESTO_EXP -> ('+' TERM RESTO_EXP) | ('-' TERM RESTO_EXP) | ε
- TERM -> FATOR RESTO_TERM
- RESTO_TERM -> ('*' FATOR RESTO_TERM) | ('/' FATOR RESTO_TERM) | ε
- FATOR -> '(' EXP ')' | num | id

## Lookahead's
- LA(S) = {'?', '!', id}
- LA(LER) = {'?'}
- LA(IMP) = {'!'}
- LA(ATRIB) = {id}
- LA(EXP) = {'(', num, id}
- LA(RESTO_EXP) = {'+', '-', ε}
- LA(TERM) = {'(', num, id}
- LA(RESTO_TERM) = {'*', '/', ε}
- LA(FATOR) = {'(', num, id}
