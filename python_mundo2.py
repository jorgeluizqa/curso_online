n1 = float(input('Dgite a nota 1: '))
n2 = float(input('Dgite a nota 2: '))
n3 = float(input('Dgite a nota 3: '))
m = (n1 + n2 + n3) / 3

print('Sua nota foi {}'.format(m))
if m >= 7:
    print('Você foi aprovado')
elif m >= 5 < 7:
    print('Você está em recuperação')
elif m < 5:
    print('Você foi reprovado')
    
