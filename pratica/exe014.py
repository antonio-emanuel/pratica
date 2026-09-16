from random import choice
print('===Exercicio 14===')
print('Entre com 4 alunos:')
n1=str(input('Nome do aluno:'))
n2=str(input('Nome do aluno:'))
n3=str(input('Nome do aluno:'))
n4=str(input('Nome do aluno:'))

lista=[n1,n2,n3,n4]
escolhido=choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))