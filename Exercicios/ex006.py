#Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número para saber o seu dobro, triplo e raiz quadrada: '))
dobro = num  * 2
triplo = num * 3
raiz_quad = num ** 2

print(f'O dobro de {num} é {dobro}.\nO triplo de {num} é {triplo}.\nA raiz quadrada de {num} é {raiz_quad}.')