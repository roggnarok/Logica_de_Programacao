#JOGO ONDE VOCÊ TEM QUE ACERTAR O NUMERO SORTEADO PELO COMPUTADOR.
from random import randint
print ("Welcome, tente adivinhar o numero de 0 a 1000")
sorteado=randint(1,1000)
chute=0
while chute!= sorteado:
    chute = int(input ("Chute: "))
    if chute == sorteado:
        print ("You Win!")
    else:
        if chute>sorteado:
            print ("Muito Alto")
        else:
            print ("Muito baixo")
print ("Game Over")
