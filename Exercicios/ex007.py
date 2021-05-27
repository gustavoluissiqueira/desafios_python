#Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e motre a sua média. 
nome_aluno = str(input('Digite seu nome:'))
nota1 = float(input((f'Aluno {nome_aluno}, digite sua nota de Português:')))
nota2 = float(input((f'Aluno {nome_aluno}, digite sua nota de Matemática:')))
media = (nota1 + nota2)/2
print(f'Aluno {nome_aluno} sua nota em Português foi de {nota1} e sua nota em Matemática foi de {nota2} e a média das duas notas foram {media}.')