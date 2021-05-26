#Desafio 003 -Crie um programa que leia dois números e mostre a soma entre eles 
nome = str(input('Digite seu nome:'))
n1 = int(input(f'{nome}, digite um número inteiro:'))
n2 = int(input(f'{nome}, digite mais um número inteiro:'))
soma = n1 + n2

print(f'{nome}, a soma entre {n1}+{n2} é igual {soma}. ')