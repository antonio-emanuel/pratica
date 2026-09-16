print('===Exercicio 29===')
velocidade=(int(input('Entre co a velocidaded do carro:')))
if velocidade>=80:
    print('Foste multado!')
    multa=velocidade/7
    print('A sua multa eh de {} kz'.format(multa))
else:
    print('Não Foi multado.')

print('==Fim===')    