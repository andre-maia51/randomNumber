import random

maxAttempts = 10
min = 1
max = 200

def generateNumber():
    return random.randint(1, 200)

def numberGuess():
    while True:
        try:
            guess = int(input(f"Digite um numero entre {min} e {max}: "))
            if min <= guess <= max:
                return guess
            else:
                print(f"Número inválido")
        except ValueError:
            print(f"Número inválido")

def checkNumber(guess, secretNumber):
    if guess == secretNumber:
        return "Correto"
    elif guess < secretNumber:
        return "O número secreto é maior"
    else:
        return "O número secreto é menor"

def playing():
    attempts = 0
    won = False

    secretNumber = generateNumber()

    while attempts < maxAttempts:
        attempts += 1
        guess = numberGuess()
        result = checkNumber(guess, secretNumber)

        if result == "Correto":
            print(f"Parabéns! O número secreto era {secretNumber}")
            won = True
            break
        else:
            print(f"{result}! Tente novamente!")


    if won == False:
        print(f"Que pena, você não tem mais tentativas! O número secreto era {secretNumber}.")

if __name__ == "__main__":
    print(f"Bem-Vind@ ao jogo da adivinhação!")
    playing()