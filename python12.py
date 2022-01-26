preço = float(input("digite o preço do produto : R$"))
promoção = preço - (preço*5 / 100)
print("O preço promocional é R$:{:.2f}".format(promoção))

