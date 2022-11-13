#COMPUTER ALGEBRA SYSTEM - CASs com SymPy. 
# The real power of a symbolic computation system such as SymPy is the ability to do all sorts of computations symbolically. SymPy can simplify expressions, compute derivatives, integrals, and limits, solve equations, work with matrices, and much, much more, and do it all symbolically. It includes modules for plotting, printing (like 2D pretty printed output of math formulas, or, code generation, physics, statistics, combinatorics, number theory, geometry, logic, and more. Here is a small sampling of the sort of symbolic power SymPy is capable of, to whet your appetite.
import sympy
from sympy import symbols
from sympy import expand, factor
from sympy import *

'''
import math
a = 9 #9  tem uma raíz exata
print(f' A Raíz quadrada de {a} é {math.sqrt(a)}. Raíz EXATA.')
b = 8 #8 não tem uma raíz exata
print(f' A Raíz quadrada de {b} é {math.sqrt(b)}. Raíz não EXATA.')

import sympy 
#Irei representar a Raíz de 8, de forma fatorada (2 x Raíz²(2))
print(f'SymPy---> A Raíz de {b} é {sympy.sqrt(b)}')
print('Raíz² de (8) = Raíz²(4*2) = 2 x Raíz²(2)')
'''

'''
#As we will see later, in SymPy, variables are defined using symbols
#Como veremos depois, no SymPy, as variáveis são definidas usando a palavra symbols
from sympy import symbols
#Abaixo X e Y serão trados como sendo variáveis do Python. Com isso, será possível fazer operações matemáticas com essas variáveis.
x, y = symbols('x y')
expr = x + 2*y
print(f'A expressão é: {expr}')

#Adicionando 1 na expressão (x + 2*y + 1)
expr = expr + 1
print(f'Adicionando 1 na expressão\
    \nA expressão agora é: {expr}')

#Subtraindo X da expressão (2*y + 1)
expr = expr - x
print(f'Subtraindo X da expressão\
    \nA expressão agora é: {expr}')
'''
'''
#No exemplo abaixo o SymPy 
# prefere manter a forma FATORADA e fazer a DISTRIBUTIVA x*(x+2y) = x² + 2xy
x, y = symbols('x y')
expr = x + 2*y
print(f'Expressão inicial {expr}')
expr = x*expr
print(f'x foi multiplicado a expressão incial')
print(expr)
#Mas existe no SymPy a possibilidade de expandir essa expressão e mostrá-la. 
# Para isso será necessário usar o método 'expand'
# Para voltar mostrar a função Fatorada, será preciso usar o método 'factor'
from sympy import expand, factor
expr = x + 2*y #Voltei para a expressão original
print(f'Expressão ORIGINAL: {expr}')
extend_expr = expand(x*expr) #Multipliquei a expressão por x e estou aplicando o método expand, para que na variável seja armazenada a expressão com a DISTRIBUTIVA feita
print(f'Expressão multiplicada por x e expandida: {extend_expr}')

#The real power of a symbolic computation system such as SymPy is the ability to do all sorts of computations symbolically
'''
from sympy import *
x, t, z, nu = symbols('x t z nu')
init_printing(use_unicode=True)

equation = sin(x)*exp(x) #Define the equation
derivada = diff(equation, x) #deriva a equação
print(f'A Derivada da equação {equation} é:\
    \n{derivada}')#mostra a derivada da equação

integral = integrate(derivada) #Integra a Derivada
print(f'A integral da equação {derivada} é:\
    \n{integral}') #Mostra a integral da equação

equation2 = sin(x**2)
integral2 = integrate(equation2, (x, -oo, oo))
print(f'A integral da equação {equation2} é:\
    \n{integral2}')

equation3 = (sin(x)/x)
limite = limit(equation3, x, 0)
print(f'O Limite da equação {equation3} é:\
    \n{limite}')

equation4 = (x**2) - 2
resolucao = solve(equation4, x)
print(f'A resolução da equação {equation4} é:\
    \n{resolucao}')

equation5 = (cos(x)**2)
integral3 = Integral(equation5, (x, 0, pi))
print(latex(integral3))
#This job was made by Rodrigo. https://github.com/roggnarok