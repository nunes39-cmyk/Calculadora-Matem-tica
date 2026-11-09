
import math


# Função responsável por receber e validar números
def ler_numero(mensagem, divisor=False):
    while True:
        try:
            entrada = input(mensagem).strip().replace(",", ".")

        except (EOFError, KeyboardInterrupt):
            print("\nPrograma encerrado pelo usuário.")
            raise SystemExit(0)

        try:
            valor = float(entrada)

        except ValueError:
            print("\nERRO: você não informou um número válido.")
            print("Digite apenas números, como 10, -5 ou 2,5.")
            print("Não utilize letras ou símbolos matemáticos neste campo.\n")
            continue

        # Impede valores infinitos, NaN e números excessivamente grandes
        if not math.isfinite(valor):
            print("\nERRO: o número informado não é válido ou é grande demais.")
            print("Digite um número finito, como 10, 100 ou 2,5.\n")
            continue

        # Impede divisão por zero
        if divisor and valor == 0:
            print("\nERRO MATEMÁTICO: divisão por zero não é permitida.")
            print("O segundo número precisa ser diferente de zero.")
            print("Exemplos válidos: 1, 2, -5 ou 0,5.\n")
            continue

        return valor


# Função responsável por realizar os cálculos
def calcular(numero1, numero2, operacao):
    try:
        if operacao == "+":
            resultado = numero1 + numero2

        elif operacao == "-":
            resultado = numero1 - numero2

        elif operacao == "*":
            resultado = numero1 * numero2

        else:
            resultado = numero1 / numero2

    except (OverflowError, ZeroDivisionError):
        return None

    # Verifica se o resultado está dentro dos limites numéricos
    if not math.isfinite(resultado):
        return None

    return resultado


# Início do programa
print("====================================")
print("       CALCULADORA MATEMÁTICA")
print("====================================")

print("\nEscolha uma das operações abaixo:")
print("+ = ADIÇÃO: soma dois números. Exemplo: 2 + 3 = 5")
print("- = SUBTRAÇÃO: subtrai o segundo número do primeiro. Exemplo: 5 - 2 = 3")
print("* = MULTIPLICAÇÃO: multiplica dois números. Exemplo: 4 * 3 = 12")
print("/ = DIVISÃO: divide o primeiro número pelo segundo. Exemplo: 8 / 2 = 4")

print("\nATENÇÃO: digite somente o símbolo da operação desejada.")


# Escolha e validação da operação
while True:
    try:
        tipocalculo = input(
            "\nDigite a operação (+, -, * ou /): "
        ).strip()

    except (EOFError, KeyboardInterrupt):
        print("\nPrograma encerrado pelo usuário.")
        raise SystemExit(0)

    if tipocalculo in ["+", "-", "*", "/"]:
        break

    print("\nERRO: operação inválida!")
    print("Você deve digitar apenas um destes símbolos:")
    print("+ para adição")
    print("- para subtração")
    print("* para multiplicação")
    print("/ para divisão")
    print("Tente novamente.\n")


# Entrada do primeiro número
print("\nOperação selecionada:", tipocalculo)
print("Agora informe os números que deseja calcular.")
print("Você pode utilizar números negativos e decimais.")

numero1 = ler_numero("\nDigite o primeiro número: ")


# Entrada do segundo número e validação do resultado
while True:
    numero2 = ler_numero(
        "\nDigite o segundo número: ",
        divisor=(tipocalculo == "/")
    )

    valor = calcular(numero1, numero2, tipocalculo)

    if valor is not None:
        break

    print("\nERRO: o resultado ultrapassa os limites numéricos suportados.")
    print("O primeiro número será mantido:", numero1)
    print("Digite um segundo número de menor magnitude.")
    print("Exemplo: tente um valor mais próximo de zero.\n")


# Resultado final
print("\n====================================")
print("           RESULTADO FINAL")
print("====================================")

print("Primeiro número:", numero1)
print("Operação:", tipocalculo)
print("Segundo número:", numero2)
print("Resultado:", valor)

print("\nCálculo concluído com sucesso!")
