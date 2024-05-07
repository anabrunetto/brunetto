def gravar_nome_em_arquivo():
    nome = input("Digite seu nome: ")

    # Abrindo o arquivo para escrita (modo "w" sobrescreve o arquivo se ele já existir)
    with open("nomes.txt", "w") as arquivo:
        arquivo.write(nome)

    print("Nome gravado com sucesso no arquivo 'nomes.txt'.")

# Chamando a função para gravar o nome em um arquivo
gravar_nome_em_arquivo()
