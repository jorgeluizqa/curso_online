from random import randint
computador = randint(0, 10)
print('Sou seu computador e acabei de pensar em um número entre 0 e 10')
print('Vovê consegue adivinhar qual é?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? :'))
    palpite += 1
    if jogador == computador:
        acertou =True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))
    