print('==Exercicio 05==')
for c in range(0,3):
    soma=0
    b=int(input('digite os numeros'))
    if (b%2==0):
        soma=soma+b
    else(b%2!=0):
        soma=soma+b    

print( 'O valor da soma dos numeros Pares eh {}'.format(soma)) 
print( 'O valor da soma dos numeros Impares eh {}'.format(soma))          
