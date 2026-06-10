 Menu de gerenciamento de lotes (apenas pares). Implemente um array de códigos de lote com o menu:
Inserir lote
Listar lotes
Retirar um lote
Limpar todos os lotes
Contar quantos lotes têm produção maior que X (X informado pelo usuário)
Verificar se um código está presente
Encontrar maior e menor código no array
Sair
Regra: o array só aceita códigos pares. Se o usuário digitar ímpar, mostre erro e volte ao menu.


lotes_cadastrados = []


while True:
    print("\n" + "="*35)
    print("1 - Inserir lote")
    print("2 - Listar lotes")
    print("3 - Retirar um lote")
    print("4 - Limpar todos os lotes")
    print("5 - Contar lotes com produção maior que X")
    print("6 - Verificar se um código está presente")
    print("7 - Encontrar maior e menor código")
    print("8 - Sair")
    print("="*35)
    
   
    opcao = input("Digite uma opção: ")

    if opcao == "1":
        codigo = int(input("Digite o código do lote (inteiro): "))
        if codigo % 2 == 0:
            lotes_cadastrados.append(codigo)
            print(f"Sucesso: Lote {codigo} inserido!")
        else:
            print("Erro: O sistema aceita apenas códigos PARES. Voltando ao menu.")

    elif opcao == "2": 
        if len(lotes_cadastrados) == 0:
            print("Nenhum lote cadastrado no momento.")
        else:
            print("Lotes:", lotes_cadastrados)

   
    elif opcao == "3": 
        if len(lotes_cadastrados) == 0:
            print("A lista está vazia. Não há o que retirar.")
        else:
            num = int(input("Digite o lote para retirar: "))
            if num in lotes_cadastrados: 
                lotes_cadastrados.remove(num) 
                print("Lote retirado com sucesso!")
            else:
                print("Lote não encontrado!")

  
    elif opcao == "4": 
        lotes_cadastrados.clear()
        print("Todos os lotes foram removidos!!!")

    elif opcao == "5": 
        if len(lotes_cadastrados) == 0:
            print("A lista está vazia.")
        else:
            x = int(input("Contar maiores que: "))
            contador = 0
            for lote in lotes_cadastrados: 
                if lote > x:
                    contador += 1 
          
            print(f"Quantidade maior que {x}: {contador}")

    
    elif opcao == "6":
        num = int(input("Digite o código para buscar: "))
        if num in lotes_cadastrados:
            print("O lote ESTÁ na lista.")
        else:
            print("O lote NÃO está na lista.")

    
    elif opcao == "7":
        if len(lotes_cadastrados) > 0:
            print("Maior código:", max(lotes_cadastrados))
            print("Menor código:", min(lotes_cadastrados))
        else:
            print("A lista está vazia. Não é possível calcular maior e menor.")

    elif opcao == "8": 
        print("Saindo do sistema... Até logo!")
      

    else:
        print("Opção inválida!!!!")
