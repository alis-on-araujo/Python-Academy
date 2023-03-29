v = float(input("Qual a velocidade do carro? "))

if v > 80:
    multa = (v - 80)*5
    print(f"Você foi multado! O valor da multa é {multa:.2f}")
else:
    print("Não foi multado")
