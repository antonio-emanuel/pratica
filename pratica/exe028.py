import random
print('===Exercicio 28===')

aleatorio=random.randint(0,5)
print('===Jogo da Sorte==== ')
numero=int(input('Entre com um numero(0 á 5)'))
if aleatorio==numero:
    print('===PARABENS!===')
    print('Numero aleatorio: {} \n Numero escrito {}'.format(aleatorio,numero))
else:
    print('===PERDEU!===')
    print('Numero aleatorio: {} \n Numero escrito {}'.format(aleatorio,numero))
    
print('===FIM DO JOGO===')    

