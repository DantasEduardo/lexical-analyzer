import tokeniza as tk


# dicionário com o nome das categorias
DESCRICAO = {
    # 7 operadores aritmético
    "^": "operador aritmético para exponenciacao" ,
    "%": "operador aritmético para resto de divisão",
    "*": "operador aritmético para multiplicação",
    "/": "operador aritmético para divisão",
    "+": "operador aritmético para adição",
    "-": "operador aritmético para subtração",
    "!": "operador aritmético 'menos unário'",
    
    # atribuicao 
    "=": "operador para atribuição",

    # parenteses: para expressões infixas */
    "(": "abre parenteses", 
    ")": "fecha parenteses", 
}

PROMPT = "expressão >>> "
QUIT   = ''

#------------------------------------------------------------
def main() -> None:
    '''
    Programa que lê do teclado uma expressão aritmética 
    e imprime cada item léxico na expressão.    
    '''
    print("Entre como uma expressão ou tecle apenas ENTER para encerrar.") 
    expressao = input(PROMPT)
    while expressao != QUIT:
        lista_tokens = tk.tokeniza(expressao)
        for token in lista_tokens:
            # pegue item e tipo
            item, tipo = token

            # cri string com a descriçao
            if tipo in [tk.OPERADOR, tk.PARENTESES]:
                print(f"'{item}' : {DESCRICAO[item]}")
            elif tipo == tk.VARIAVEL:
                print(f"'{item}' : nome de variável")
            elif tipo == tk.NUMERO:
                print(f"{item} : constante float")
            else:
                print(f"'{item}' : categoria desconhecida")

        # leia próxima expressão    
        expressao = input(PROMPT)        


#-------------------------------------------
# início da execução do programa
if __name__ == "__main__":
    main()
        
