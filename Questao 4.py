def digitar_nomes():
    nomes = []  # Lista para armazenar os nomes

    # Loop infinito até que 'sair' seja digitado
    while True:
        nome = input("Digite um nome ou 'sair' para encerrar: ")
        if nome.lower() == 'sair':
            break  # Encerra o loop se 'sair' for digitado
        nomes.append(nome)

    # Imprime todos os nomes digitados, cada um em uma linha
    for nome in nomes:
        print(nome)

# Exemplo de uso:
digitar_nomes()