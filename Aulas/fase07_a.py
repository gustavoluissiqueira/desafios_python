#Aula 07 - Operadores Aritméticos

#Operadores Aritméticos
                         #Operandos
# + = Adicao                    5   +   2 == 7
# - = Subtração                 5   -   2 == 3
# * = Multiplicação             5   *   2 == 10 
# / = Divisão                   5   /   2 == 2.5 
# ** = POTÊNCIA                 5   **  2 == 25 
# // = Divisão inteira          5   //  2 == 2       5/2
#                                                    1|2
# % = Resto da Divisão          5   %   2 == 1 

#oRDEM DE PRECEDêNCIA 
# 1 -> ()
# 2 -> **
# 3 -> * / // %
# 4 -> + -

# a = 5+3*2
# b = 5**2
# c = 5**3
# d = 19//2
# e = 19/2
# f = 365**522
# g = 18%2
# h = 122%3
# i = 4**3
# j = pow(4,3)
# print(j)
# k = 81**(1/2)
# print(k)
# aa = 25**(1/2)
# print(aa)
# bb = "oi"+"olá"
# print(bb)
# cc = "oi"*5
# print(cc)

# nome = input('Qual é o seu nome?')
# print(f'Prazer em te conhecer {nome:=^20}!')
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s =  n1+n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma vale {s}, a multiplicação é {m}, a divisão é {d:.3f}, a Divisão inteira é  {di} e a potência é {e}.')

