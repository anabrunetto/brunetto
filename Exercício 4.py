def encontrar_nome_por_numero(numero, nome_arquivo):
    try:
        # Abrindo o arquivo para leitura (modo "r" para leitura)
        with open(nome_arquivo, "r") as arquivo:
            # Lendo todas as linhas do arquivo
            linhas = arquivo.readlines()

            # Verificando se o número está dentro do intervalo válido
            if 0 < numero <= len(linhas):
                # Obtendo o nome correspondente ao número
                nome = linhas[numero - 1].strip()
                print(f"O nome correspondente ao número {numero} é: {nome}")
            else:
                print("Número inválido. Forneça um número dentro do intervalo válido.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

# Chamando a função para encontrar o nome correspondente ao número
numero = int(input("Digite um número: "))
encontrar_nome_por_numero(numero, "enumerados.txt.txt")