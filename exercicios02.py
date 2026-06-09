Últimas colheitas invertidas. Peça 5 valores de produção (kg de azeitona) informados pelo usuário, armazene em um array e imprima na ordem inversa.


vetor= []
soma = 0 
for i in range (5):
    producao=float(input("Digite a produção de azeitonas? "))
    vetor.append(producao)
vetor_invertido = vetor [:: - 1]

print("Em ordem invertida: ", )
print("Vetor_invertido:", vetor_invertido )
