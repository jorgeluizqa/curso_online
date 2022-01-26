dia = float(input('Digite a quantidade de dias: '))
KM = float(input('Digite a quantidade de KM rodados: '))
diária = 60.00
KMr = 0.15
custo = dia * diária + KM * KMr
print('O custo total da locação foi R${:.2f}'.format(custo))