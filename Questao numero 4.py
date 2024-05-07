def celsius_para_fahrenheit():
    # Solicitar ao usuário a temperatura em graus Celsius
    celsius = float(input("Digite a temperatura em graus Celsius: "))

    # Converter de Celsius para Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Imprimir o resultado
    print("A temperatura em Fahrenheit é:", fahrenheit, "°F")

# Exemplo de uso:
celsius_para_fahrenheit()
