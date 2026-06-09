Verificar lote na lista de inspeção. Crie um array com 5 códigos de lote (inteiros). 
Depois, peça um código e verifique se ele está presente no array (informar “encontrado”/“não encontrado”).


lote_inspecao=[]

print("Cadrastro de lotes ....")
for n in range(0,10):
    lotes = float(input("Digite um numero para o lote? "))
    lote_inspecao.append(lotes)
print("\n--- Sistema de Busca/Inspeção ---")
busca = float(input("Digite o código do lote que deseja verificar se existe? "))

if lotes in lote_inspecao:
    print("Resultado: Encontrado")
else:
    print("Resultado: Não encontrado")
