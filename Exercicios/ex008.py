#Desafio 007 - Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milimetros.
metros = float(input('Quanto metros tem:'))
cm = metros / 0.010000
mm = metros / 0.001

print(f'Convertendo {metros} metros para centímetros é igual a {cm}cm e em milimetros é igual a {mm}mm')
