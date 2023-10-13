print("*********************************")
print("bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chut_str = input("digite seu numero:")

print("voce digitou", chut_str)

chute =int(chut_str)

acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("voce acertou")
else: 
    if(maior):
        print("voce errou! O seu numero foi maior que o numero secreto.")
    elif(chute < numero_secreto):
        print("voce errou! O seu numero foi menor que o numero secreto.")


print("fim de jogo")

