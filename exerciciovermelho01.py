
Leia um array com 8 valores de produção de azeitonas em kg. Calcule a média e exiba quais produções ficaram acima da média.

vetor= []
soma = 0 
for i in range (8):
    qtd=float(input("Digite o quantidade de azeitonas? "))
    vetor.append(qtd)
    soma = soma + qtd

media = soma / 2

print("Media de azeitonas: ", media)
