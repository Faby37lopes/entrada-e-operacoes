# Entrada de dados
dado1 = input("Digite o primeiro dado: ")
dado2 = input("Digite o segundo dado: ")
resultado = dado1 + dado2
print("Resultado da concatenação:", resultado)

print("\n---\n")

# Repetição de texto
texto = input("Digite uma palavra ou frase: ")
vezes = int(input("Quantas vezes você quer repetir? "))
print("Resultado da repetição:")
print(texto * vezes)

print("\n---\n")

# Operações matemáticas
print("Escolha uma operação matemática:")
print("1 - Multiplicação")
print("2 - Divisão")
print("3 - Diferença Absoluta")

opcao = int(input("Digite a opção (1, 2 ou 3): "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == 1:
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)

elif opcao == 2:
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: divisão por zero.")

elif opcao == 3:
    resultado = abs(num1 - num2)
    print("Resultado da diferença absoluta:", resultado)

else:
    print("Opção inválida.")
