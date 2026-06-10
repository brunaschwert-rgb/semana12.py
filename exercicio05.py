Valor por árvore (kg × preço). Leia dois arrays de 5 elementos:
kg_colhidos (produção por árvore)
preco_por_kg (preço do cultivar/qualidade correspondente)
Crie um terceiro array com a multiplicação elemento a elemento (valor obtido por árvore).


kg_colhidos = []
preco_por_kg = []
valor_por_arvore = []

for i in range(5):
    colhidos= float(input("Digite a quantidade de kg colhidos? "))
    kg_colhidos.append(colhidos)
for i in range(5):
    preco= float(input("Digite o preço por kg? "))
    preco_por_kg.append(preco)
for i in range(5):
    total_arvore = kg_colhidos[i] * preco_por_kg[i]
    valor_por_arvore.append(total_arvore)

print("faturamento por árvore ")
for i in range(5):
    print(f"Árvore {i+1}: R$ {valor_por_arvore[i]:}")
