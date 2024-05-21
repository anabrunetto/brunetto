def numeros_pares(n):
    # Verifica se n é menor que 2, caso em que não há números pares entre 1 e n
    if n < 2:
        return []
    
    # Gera a lista de números pares entre 2 e n, inclusive
    pares = list(range(2, n + 1, 2))
    
    return pares

# Exemplo de uso:
numero = 10
print(numeros_pares(numero))  # Saída: [2, 4, 6, 8, 10]