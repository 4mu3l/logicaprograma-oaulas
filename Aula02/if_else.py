# concatenação
# quebra de linha
# formatando decimais
# alterando virgula e ponto
# if else
# operador ternario
# FIXME - concatenação com +
'''
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
print(30*"-")
#variaveis
nome= input('digite seu nome ')
idade= int(input('digite sua idade '))
#estrutura de decisão
if idade >= 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} é menor de idade')
print(50*"-")
#BOLETIM ESCOLAR COM IF, ELSE E ELIF
print(40*"-","BOLETIM ESCOLAR", 40*"-")
nome_aluno = input("Digite o nome do aluno ")
nota1 = float(input("Digite sua nota "))
nota2 = float(input("Digite sua nota "))
nota3 = float(input("Digite sua nota "))
nota4 = float(input("Digite sua nota "))
media = (nota1+nota2+nota3+nota4)/4
#>=7: aprovado
#>=5: recuperação
#reprovado
if media >=7:
    print(f'{nome_aluno} aluno aprovado!')
    print(f'nota 1; {nota1}| nota 2: {nota2}')
    print(f'nota 3: {nota3}| nota 4: {nota4}')
    print(20*'-')
    print(f"media: {media}")
elif media >=5:
    print(f'{nome_aluno} aluno recuperação!')
    print(f'nota 1:{nota1}| nota 2: {nota2}')
    print(f'nota 3:{nota3}| nota 4: {nota4}')
    print(20*'-')
    print(f"media: {media}")
else:
    print(f'{nome_aluno} aluno reprovado!')
    print(f'nota 1{nota1}| nota 2: {nota2}')
    print(f'nota 3{nota3}| nota 4: {nota4}')
    print(20*'-')
    print(f"media: {media}")
'''
'''
#MONTANHA RUSSA
#variaveis
nome = input("Digite seu nome ")
idade = float(input("Digite sua idade "))
altura = float(input("Digite sua altura ").replace(",","."))
altura =float(altura)
# verificação dos requsitos
if idade >= 12 and altura>= 1.2:
    print(f"É concedido a entrada de {nome} para a montanha russa")
else:
    print(f"A permissão para a entrada recusada, melhore!!!")
'''
# variaveis
nome= 'alex'
idade = 19
print(nome,'maior de idade,' if idade >= 18 else 'é menor de idade')