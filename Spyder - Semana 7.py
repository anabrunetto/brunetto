def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    return [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]

def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Exemplos de uso
if __name__ == "__main__":
    # Questão 1
    lista_numeros = [1, 2, 3, 4]
    soma, media = calcular_soma_e_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    # Questão 2
    lista_palavras = ["banana", "morango", "limão"]
    palavra_antiga = "banana"
    palavra_nova = "maçã"
    lista_alterada = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
    print("Lista alterada:", lista_alterada)

    # Questão 3
    num_linhas = 4
    gerar_triangulo(num_linhas)

