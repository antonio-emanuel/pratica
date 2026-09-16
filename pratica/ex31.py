print('==Eprestimo Bancário===')
valorCasa=float(input('Digite o valor da casa:'))
salario=float(input('Informe o teu salário:'))
anoPagamento=int(input('Quantos anos deseja pagar a casa? '))
novo=(salario*30/100)
prestacao=valorCasa/anoPagamento
if prestacao>novo:
    print('Imprestimo Negado!')
else:
    print('Imprestimo Aceito!')
    print('Valor da prestação mensal: {} kz '.format(prestacao))