def imprimir_conteudo_arquivo():
    nome_arquivo = input("Digite o nome do arquivo de texto: ")

    # Abrindo o arquivo para leitura (modo "r" para leitura)
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

# Chamando a função para imprimir o conteúdo do arquivo
imprimir_conteudo_arquivo()