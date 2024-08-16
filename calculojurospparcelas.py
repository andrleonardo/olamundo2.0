print("Bem-vindo a loja da jejeh")
valor = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

if quantidadeParcelas < 4:
    juros = 4 / 100
elif quantidadeParcelas < 9:
    juros = 8 / 100
elif quantidadeParcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

    valorp = (valor * (1 + juros)) / quantidadeParcelas
valortotalp = valorp * quantidadeParcelas


print("O valor das parcelas é de: R$ {:.2f}".format(valorp))
print("O valor Total Parcelado é de: R$ {:.2f}".format(valortotalp))
