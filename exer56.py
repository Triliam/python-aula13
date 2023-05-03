#valor1 = int(input("Digite o primeiro valor"))
#valor2 = int(input("Digite o segundo valor"))
#valor3 = int(input("Digite o terceiro valor"))

#media = (valor1 + valor2 + valor3) / 3

#print(media)

soma = 0.0
qtdNotas = 5

for i in range(qtdNotas):
    nota = float(input("Qual a nota ? "))
    soma = soma + nota

media = soma/qtdNotas

print("A média é: ", media)