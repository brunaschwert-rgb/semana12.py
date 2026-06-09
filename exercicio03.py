Soma de fazendas. Crie dois arrays do mesmo tamanho com produções inteiras (kg) de Fazenda A e Fazenda B.
Gere um terceiro array com a soma elemento a elemento (produção total por posição/lote).

vetor= []
fazendaA= []
fazendaB= []
pdc_total = []
for i in range (4):
    valor=float(input("Digite a produção de lote da fazendaA (kg)? "))
    fazendaA.append(valor)

for i in range (4):
    valor=float(input("Digite a produção de lote da fazendaB (kg)? "))
    fazendaB.append(valor)

for i in range (4):
   soma_lote = fazendaA[i] + fazendaB[i]
   pdc_total.append(soma_lote)

print("\n--- Resultado Final ---")
print("Fazenda A:", fazendaA)
print("Fazenda B:", fazendaB)
print("Produção Total: ", pdc_total)
