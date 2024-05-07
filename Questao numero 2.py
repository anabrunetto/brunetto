def calcular():
    # Pedir ao usuário dois números e a operação desejada
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Calcular o resultado com base na operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:  # Verificar se o segundo número não é zero para evitar divisão por zero
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero!")
            return  # Encerrar a função se houver divisão por zero
    else:
        print("Operação inválida!")
        return  # Encerrar a função se a operação for inválida

    # Imprimir o resultado
    print("O resultado de", num1, operacao, num2, "é:", resultado)

# Exemplo de uso:
calcular()

