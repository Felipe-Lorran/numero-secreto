print("******************************")
print("bem vindo ao jogo de adivinhar")
print("******************************")
 
numero_secreto = 70

chut_str = input("digite um numero")
print("voce digitou", chut_str)

chute = int(chut_str)

acertou = numero_secreto == chute 
maior  = chute > numero_secreto
menor  = chute < numero_secreto

if(acertou):
    print("voce acertou")
else:
    if(maior):
        print("voce errou! O numero é maior que numero secreto.")
    if(menor):
        print("voce errou! O numero é menor que o numero secreto.")



print("lorran é o melhor")




