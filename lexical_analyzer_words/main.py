import tokeniza_words as tk


#------------------------------------------------------------
def main(event, context) -> None:
    tokens = tk.get_feling(event['Text'])
    print(tokens)


#-------------------------------------------
# início da execução do programa
if __name__ == "__main__":
    t = """Deu no @presenterural: estudo mostra que a demanda japonesa por soja convencional para consumo humano poderá ser de 230 mil toneladas em dez anos.
    """
    e = {"Text": t}
    main(e, "context")
        