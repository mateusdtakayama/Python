dias = int(input("Quantos dias foram usados o carro? "))
kms = float(input("Quantos kms foram rodadoss? "))

preco = 60*dias + 0.15*kms

print(f"O preço a ser pago é R${preco:.2f}")