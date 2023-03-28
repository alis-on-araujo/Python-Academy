#função para converter celsius para fahrenheit

def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius) / 5 + 32
    return fahrenheit

TF = celsius_para_fahrenheit(0)
print(TF)
