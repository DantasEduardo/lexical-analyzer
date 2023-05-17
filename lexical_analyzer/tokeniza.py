import re


# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')


def tokeniza(exp:str) -> tuple:
    """
    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria. 

        - 1 sendo OPERADOR;
        - 2 sendo NUMERO; 
        - 3 sendoVARIAVEL; ou 
        - 4 sendo PARENTESES

    A funçao ignora tudo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    
    tokens = []
    for i in re.findall(r'(\d+\.\d+|\d+|[\+\-\*\/\%\&\|\^\~\<\>\=\()]|[a-zA-Z_][a-zA-Z0-9_]*)', exp.split("#")[0]):
        if re.match(r'[+\-*/=]', i):
            tokens.append((i, OPERADOR))
        elif re.match(r'\d+(\.(\d+)?)?', i):    
            tokens.append((float(i), NUMERO))
        elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', i):    
            tokens.append((i, VARIAVEL))
        elif re.match(r'[()]', i):    
            tokens.append((i, PARENTESES))

    return tokens

