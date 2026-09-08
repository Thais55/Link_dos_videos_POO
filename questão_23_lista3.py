#Recebe dez codigos inteiros armazena e informa quantas vezes cada codigo apareceu

#Criar a lista 
codigos = []

# Primeiro: digitar os 10 códigos
for i in range(10):
    codigo = int(input(f"Digite o {i + 1} código: "))
    codigos.append(codigo)

# Depois que os 10 códigos foram digitados
verificados = []

print("\nQuantidade de ocorrências:")

for codigo in codigos:
    if codigo not in verificados:
        quantidade = codigos.count(codigo)

        print(f"Código {codigo}: {quantidade} vez(es)")

        verificados.append(codigo)


