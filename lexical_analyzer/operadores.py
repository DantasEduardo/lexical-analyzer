'''
   NÃO MODIFIQUE ESTE ARQUIVO - autor MAC0122
   
   Este arquivo contém um dicionário com a descrição dos 
   itens léxicos correspondentes a operadores e parenteses.
'''

#-------------------------------------------------------------
# 
#  C O N S T A N T E S 
#

'''
   temos 13 categorias de itens léxicos sendo: 

       - 8 para operadores, 
       - 2 para o abre e fecha parenteses  
'''

# 7 operadores aritméticos  
OPER_RESTO_DIVISAO  = "%"
OPER_MULTIPLICACAO  = "*"
OPER_DIVISAO        = "/"
OPER_ADICAO         = "+"
OPER_SUBTRACAO      = "-"
OPER_MENOS_UNARIO   = "!" 
OPER_EXPONENCIACAO  = "^" 

# atribuicao 
OPER_ATRIBUICAO     = "=" 

# parenteses: para expressões infixas 
ABRE_PARENTESES     = "(" 
FECHA_PARENTESES    = ")" 


# dicionário com o nome das categorias
DESCRICAO = {
    # 7 operadores aritmético
    OPER_EXPONENCIACAO: "operador aritmético para exponenciacao" ,
    OPER_RESTO_DIVISAO: "operador aritmético para resto de divisão",
    OPER_MULTIPLICACAO: "operador aritmético para multiplicação",
    OPER_DIVISAO:       "operador aritmético para divisão",
    OPER_ADICAO:        "operador aritmético para adição",
    OPER_SUBTRACAO:     "operador aritmético para subtração",
    OPER_MENOS_UNARIO:  "operador aritmético 'menos unário'",
    
    # atribuicao 
    OPER_ATRIBUICAO:   "operador para atribuição",

    # parenteses: para expressões infixas */
    ABRE_PARENTESES:   "abre parenteses", 
    FECHA_PARENTESES:  "fecha parenteses", 
}
