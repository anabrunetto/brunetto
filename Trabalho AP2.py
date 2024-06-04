def ler_arquivo():
    # Função para ler o arquivo de registro e retornar os dados como uma lista de tuplas
    with open("registro.txt", "r") as arquivo:
        dados = [linha.strip().split(",") for linha in arquivo]
    return dados

def buscar_por_nome(texto):
    # Função para buscar clientes pelo texto informado no nome
    dados = ler_arquivo()
    nomes = set()
    for linha in dados:
        if texto.lower() in linha[0].lower():
            nomes.add(linha[0])
    for nome in nomes:
        print(nome)

def buscar_por_nome_completo(nome_completo):
    # Função para buscar casos associados a um cliente pelo nome completo
    dados = ler_arquivo()
    for linha in dados:
        if nome_completo.lower() == linha[0].lower():
            print("Número do caso:", linha[1])

def informar_detalhes_caso(numero_caso):
    # Função para informar os detalhes de um caso pelo número do caso
    dados = ler_arquivo()
    for linha in dados:
        if numero_caso == linha[1]:
            nome_cliente, despesa, receita = linha[0], float(linha[2]), float(linha[3])
            diferenca = receita - despesa
            print("Nome do cliente:", nome_cliente)
            print("Despesa:", despesa)
            print("Receita:", receita)
            print("Diferença entre receita e despesa:", diferenca)

def calcular_despesa_total():
    # Função para calcular e imprimir a despesa total
    dados = ler_arquivo()
    despesa_total = sum(float(linha[2]) for linha in dados[1:])  # Ignora a primeira linha
    print("Despesa total:", despesa_total)

def calcular_receita_total():
    # Função para calcular e imprimir a receita total
    dados = ler_arquivo()
    receita_total = sum(float(linha[3]) for linha in dados[1:])  # Ignora a primeira linha
    print("Receita total:", receita_total)

def caso_com_maior_despesa():
    # Função para imprimir os detalhes do caso com a maior despesa
    dados = ler_arquivo()[1:]  # Ignora a primeira linha (cabeçalho)
    maior_despesa = max(float(linha[2]) for linha in dados)
    for linha in dados:
        if float(linha[2]) == maior_despesa:
            print("Nome do cliente:", linha[0])
            print("Número do caso:", linha[1])
            print("Receita:", linha[3])
            print("Despesa:", linha[2])

def caso_com_maior_receita():
    # Função para imprimir os detalhes do caso com a maior receita
    dados = ler_arquivo()[1:]  # Ignora a primeira linha (cabeçalho)
    maior_receita = max(float(linha[3]) for linha in dados)
    for linha in dados:
        if float(linha[3]) == maior_receita:
            print("Nome do cliente:", linha[0])
            print("Número do caso:", linha[1])
            print("Receita:", linha[3])
            print("Despesa:", linha[2])

def salvar_detalhes_cliente(nome_completo):
    # Função para salvar os detalhes dos casos associados a um cliente em um arquivo
    dados = ler_arquivo()
    with open(nome_completo + "_detalhes.txt", "w") as arquivo:
        total_despesas = 0
        total_receitas = 0
        for linha in dados:
            if nome_completo.lower() == linha[0].lower():
                arquivo.write("Número do caso: {}\n".format(linha[1]))
                arquivo.write("Despesa: {}\n".format(linha[2]))
                arquivo.write("Receita: {}\n".format(linha[3]))
                total_despesas += float(linha[2])
                total_receitas += float(linha[3])
        arquivo.write("Total de despesas: {}\n".format(total_despesas))
        arquivo.write("Total de receitas: {}\n".format(total_receitas))
        arquivo.write("Diferença entre receitas e despesas: {}\n".format(total_receitas - total_despesas))
    print("Detalhes salvos com sucesso!")

def exibir_menu():
    # Função para exibir o menu e solicitar a escolha do usuário
    print("\nMenu:")
    print("a) Buscar por parte do nome do cliente")
    print("b) Buscar casos associados a um cliente pelo nome completo")
    print("c) Informar detalhes de um caso pelo número do caso")
    print("d) Calcular e imprimir a despesa total")
    print("e) Calcular e imprimir a receita total")
    print("f) Imprimir os detalhes do caso com a maior despesa")
    print("g) Imprimir os detalhes do caso com a maior receita")
    print("h) Salvar detalhes dos casos associados a um cliente em um arquivo")
    print("sair) Sair do programa")
    escolha = input("Escolha a opção (a-h): ").lower()
    return escolha

def main():
    opcao = ""
    while opcao != "sair":
        opcao = exibir_menu()
        if opcao == "a":
            texto = input("Digite a parte do nome a ser buscada: ")
            buscar_por_nome(texto)
        elif opcao == "b":
            nome_completo = input("Digite o nome completo do cliente: ")
            buscar_por_nome_completo(nome_completo)
        elif opcao == "c":
            numero_caso = input("Digite o número do caso: ")
            informar_detalhes_caso(numero_caso)
        elif opcao == "d":
            calcular_despesa_total()
        elif opcao == "e":
            calcular_receita_total()
        elif opcao == "f":
            caso_com_maior_despesa()
        elif opcao == "g":
            caso_com_maior_receita()
        elif opcao == "h":
            nome_completo = input("Digite o nome completo do cliente: ")
            salvar_detalhes_cliente(nome_completo)
        elif opcao == "sair":
            print("Saindo do programa...")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
