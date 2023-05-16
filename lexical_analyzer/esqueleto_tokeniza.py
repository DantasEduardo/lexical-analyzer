
# Constantes
TESTE   = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS  = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR   = 1 # para operadores aritméticos e atribuição
NUMERO     = 2 # para números: todos são considerados float
VARIAVEL   = 3 # para variáveis
PARENTESES = 4 # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS    = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"


#------------------------------------------------------------
def tokeniza(exp):
    """(str) -> list

    Recebe uma string exp representando uma expressão e cria 
    e retorna uma lista com os itens léxicos que formam a
    expressão.

    Cada item léxico (= token) é da forma
       
        [item, tipo]

    O componente item de um token é 

        - um float: no caso do item ser um número; ou 
        - um string no caso do item ser um operador ou 
             uma variável ou um abre/fecha parenteses.

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima). 

        - OPERADOR;
        - NUMERO; 
        - VARIAVEL; ou 
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo
    
