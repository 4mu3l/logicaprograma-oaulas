# concatenação
# quebra de linha
# formatando decimais
# alterando virgula e ponto
# if else
# operador ternario
# FIXME - concatenação com +

nome = "Gomes"
idade = 26
altura = 1.75
# saida de dados
print("Olá, meu nome é "+ nome +"minha idade é " + str(idade))

#FIXME - concatenação com ,
print("Olá, meu nome é,", nome, "tenho", idade, "anos de idade")

#FIXME - concatenação com format
print("Olá, meu nome é, {}, tenho {} idade".format(nome, idade))

#FIXME - concatenação com f-string
print(f"Olá, meu nome é {nome} e tenho {idade} anos de idade")

# eliminando a quebra de linha
print("O sábio sabia ", end="")
print ("que o sabiá sabia assobiar.")


valor = 1.23456789
# exibindo o valor com duas casas decimais
print(f"{valor:,.2f}")

print(30*"-")
peso = input("digite seu peso: ").replace(",",".")
peso = float(peso)
print(f'Esse peso é o seu mesmo {peso}'.replace(".",","))


