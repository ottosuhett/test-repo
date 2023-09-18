# \n
kg = float(input("Digite seu peso em kg: "))
alt = float(input("Digite sua altura em metros: "))
def calculoImc(peso, altura):
    imc = peso/(altura * altura)
    total = round(imc,2)
    return total

res = calculoImc(kg,alt)
print(res)