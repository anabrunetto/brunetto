import random

def advinhe_o_numero():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0
    acertou = False
    print("Adivinhe o número entre 1 e 100")
    
    while not acertou:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < numero_aleatorio:
            print("Muito baixo!")
        elif palpite > numero_aleatorio:
            print("Muito alto")
        else:
            print(f"Você adivinhou em {tentativas} tentativas.")
            acertou = True

def sorteio_premios():
    premios = ["Carro", "Viagem", "Notebook", "Smartphone"]
    participantes = input("Digite seu nome:")
    premio = random.choice(premios)
    print(f"Parabéns, {participantes}! Você ganhou um(a) {premio}.")