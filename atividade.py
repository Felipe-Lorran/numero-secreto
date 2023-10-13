print("****************************")
print("welcome to the guessing game")
print("****************************")

numero_secreto = 55

chut_str = input ("digite um numero")

print("voce digitou", chut_str)

chute = int ( chut_str)

acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("voce acertou")
else:
    if(maior):    
         print("voce errou! O numero foi maior que o numero secreto.")
    if(menor):
        print("voce errou! O numero foi menor que o numero secreto.") 

print("FELIPE LORRAN É O MELHOR")


