'''
Programa recebe os valores de X e Y e mostra se o ponto está no eixo X, eixo Y, no 1º, 2º, 3º ou 4º quadrante.
'''
while True:
    x = float(input('digite x:'))
    y = float(input('digite y:'))

    if x == 0 and (y == 0):
        print('Origem')
    elif (x > 0) and (y == 0):
        print('Eixo X positivo')
    elif (x < 0) and (y == 0):
        print('Eixo X negativo')
    elif (x == 0) and (y > 0):
        print('Eixo Y positivo')
    elif (x == 0) and (y < 0):
        print('Eixo Y negativo')
    elif (x > 0) and (y > 0):
        print('Primeiro quadrante')
    elif (x < 0) and (y > 0):
        print('Segundo quadrante')
    elif (x < 0) and (y < 0):
        print('Terceiro quadrante')
    elif (x > 0) and (y < 0):
        print('Quarto quadrante')
#This job was made by Rodrigo. https://github.com/roggnarok

