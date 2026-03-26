"Calculador Simples em Python"

# float em Python representa números de ponto flutuante,
#ou seja, números reais que possuem casas decimais

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
operação = input("Digite a operação (+, -, *, /):")

if operação == "+":
    resultado = num1 + num2
elif operação == "-":
    resultado = num1 - num2
elif operação == "*":   
    resultado = num1 * num2
elif operação == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação inválida "

print("O resultado é", resultado)

while True:
    resposta = input("Deseja realizar outra operação ? (s/n):")
    if resposta == "s" or resposta == "S":
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        operação = input("Digite a operação (+, -, *, /):")
    elif resposta == "n" or resposta == "N":
        break

    print ("O resultado é", resultado)