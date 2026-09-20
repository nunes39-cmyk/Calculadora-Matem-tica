while True:
  tipocalculo = input("Digite o Tipo de calculo (Divisão ou / ou ÷, Multiplicação ou x ou *, Adição ou +, Subtração ou -.).: ").lower()
  
  if tipocalculo not in ["divisão", "/","÷", "-", "+", "*", "x", "multiplicação", "adição", "subtração"]:
    print("Tipo de calculo inválido. Tente novamente.") 
  else:
    break
    
while True:
  try:
    numero1 = float(input("Digite apenas números(primeiro valor do calculo): ").replace(",", "."))
  except:
    print("Você deve digitar apenas número! Seja ele inteiro ou Decimal.")
  else:
    break
 
while True:
  try:
    numero2 = float(input("Digite apenas números(segundo valor do calculo): ").replace(",", "."))
  except:
    print("Você deve digitar apenas número! Seja ele inteiro ou Decimal.")
  else:
    break

if tipocalculo == "divisão" or "/" or "÷":
  if numero1 == 0 and numero2 == 0:
    print("Erro")
  elif numero2 == 0:
    print("Infinity")
  else:
    valor = numero1 / numero2
    print("O valor do caucolo é:", valor)

elif tipocalculo == "multiplicação" or "x" or "*":
  valor = numero1 * numero2
  print("O valor do calculo é:", valor)

elif tipocalculo == "adição" or "+":
  valor = numero1 + numero2
  print("O valor do calculo é:", valor)

elif tipocalculo == "subtração" or "-":
  valor = numero1 - numero2
  print("O valor do calculo é:", valor)

else:
  print("Tipo de cálculo inválido.")