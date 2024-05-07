def copiar_conteudo_arquivo(nome_arquivo_origem, nome_arquivo_destino):
    try:
        # Abrindo o arquivo de exemplo para leitura (modo "r" para leitura)
        with open(nome_arquivo_origem, "r") as arquivo_origem:
            # Lendo o conteúdo do arquivo de exemplo
            conteudo = arquivo_origem.read()

            # Abrindo o novo arquivo para escrita (modo "w" para escrita)
            with open(nome_arquivo_destino, "w") as arquivo_destino:
                # Escrevendo o conteúdo no novo arquivo
                arquivo_destino.write(conteudo)

        print(f"O conteúdo do arquivo '{nome_arquivo_origem}' foi copiado para '{nome_arquivo_destino}'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_origem}' não foi encontrado.")

# Chamando a função para copiar o conteúdo do arquivo
copiar_conteudo_arquivo("nomes.txt", "novo.txt")