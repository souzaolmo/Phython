entrada = input('digite um numero: ') 
if entrada.isdigit():
    entrada_int= int(entrada)
    par_impar = entrada_int %2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O número{entrada_int} é {par_impar_texto}')
else:
    print('você não digitou um numero inteiro')  
try:
    entrada_int = float(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

         print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')
