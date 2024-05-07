def lista_de_compras():
    # Pedir ao usuário para digitar os itens da lista de compras separados por vírgula
    itens = input("Digite os itens da lista de compras, separados por vírgula: ")

    # Dividir a entrada do usuário em uma lista de itens
    lista_compras = itens.split(',')

    # Imprimir os itens em linhas separadas usando um loop
    for i, item in enumerate(lista_compras, start=1):
        print("Item", i, ":", item.strip())

# Exemplo de uso:
lista_de_compras()
