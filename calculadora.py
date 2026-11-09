
while True:
    tipocalculo = input("Digite o tipo de cálculo (Divisão ou / ou ÷, Multiplicação ou x ou *, Adição ou +, Subtração ou -): ").strip().lower()

    if tipocalculo not in ["divisão", "/", "÷", "-", "+", "*", "x", "multiplicação", "adição", "subtração"]:
        print("Tipo de cálculo inválido. Tente novamente.")
    else:
        break

while True:
    try:
        numero1 = float(input("Digite apenas números (primeiro valor do cálculo): ").replace(",", "."))
    except ValueError:
        print("Você deve digitar apenas números! Sejam eles inteiros ou decimais.")
    else:
        break

while True:
    try:
        numero2 = float(input("Digite apenas números (segundo valor do cálculo): ").replace(",", "."))
    except ValueError:
        print("Você deve digitar apenas números! Sejam eles inteiros ou decimais.")
    else:
        break

if tipocalculo in ["divisão", "/", "÷"]:
    if numero1 == 0 and numero2 == 0:
        print("Erro: não é possível dividir zero por zero.")
    elif numero2 == 0:
        print("Erro: não é possível dividir por zero.")
    else:
        valor = numero1 / numero2
        print("O valor do cálculo é:", valor)

elif tipocalculo in ["multiplicação", "x", "*"]:
    valor = numero1 * numero2
    print("O valor do cálculo é:", valor)

elif tipocalculo in ["adição", "+"]:
    valor = numero1 + numero2
    print("O valor do cálculo é:", valor)

elif tipocalculo in ["subtração", "-"]:
    valor = numero1 - numero2
    print("O valor do cálculo é:", valor)

else:
    print("Tipo de cálculo inválido.")
