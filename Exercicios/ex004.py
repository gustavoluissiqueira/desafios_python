#Desafio 004 -  Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela. 
nome = str(input('Digite seu nome para você saber sobre os tipos primitivos:'))

tipo = input(f'{nome}, digite alguma coisa:')
print(f'é qual tipo?{type(tipo)}')
print(f'Tem espaço? {tipo.isspace()}')
print(f'É alphanumerico? {tipo.isalnum()}')
print(f'É maiúsculo? {tipo.isupper()}')
print(f'É minúscula? {tipo.isupper()}')
print(f'É numérico? {tipo.isnumeric()}')
