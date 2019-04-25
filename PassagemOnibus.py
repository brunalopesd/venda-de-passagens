def limpar_tela ():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')    
       
def poltronas ():
    print ()
    print ('Lugares vagos [0] - Lugares ocupados [x]')
    print ()
    print ('Janela Direita:    ', janela_direita)
    print ('Janela Esquerda:   ', janela_esquerda)
    print ('Corredor Direita:  ', corredor_esquerda)
    print ('Corredor Esquerda: ', corredor_esquerda)
    print ()

def menu_passagem ():
    print('       ----M E N U----')
    print('''    [ 1 ] Vender passagem
    [ 2 ] Finalizar Vendas
    [ 3 ] Sair
    [ 4 ] Ver poltronas''')
    

janela_direita = [0] * 3
corredor_direita = [0] * 3
janela_esquerda = [0] * 3
corredor_esquerda = [0] * 3
pass_meia = 0     
pass_inteira = 0
total_vendido = 0
def vender_passagem ():
    global total_vendido
    global pass_meia    
    global pass_inteira
    while(total_vendido <= 12):
        print ()
        idade = int(input('Qual a idade do passageiro?: '))
        if (idade < 5 or idade > 65):
            pass_meia = pass_meia + 1
        else:
            pass_inteira = pass_inteira + 1     
        opcao = str(input("Digite opcao Janela [ J ] ou Corredor [ C ]?: "))
        if opcao == "j" or opcao == "J":
            opcao2 = str(input('Janela direita ou esquerda JD/JE: '))
            if opcao2 == 'jd' or opcao2 == 'JD':
                if janela_direita == ['x', 'x' , 'x']:
                    print ('Todos os lugares estão ocupados!')
                    break
                print("Posicoes livres na janela:")
                for i in range(3):
                    if janela_direita[i] == 0:
                        print((i+1),end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                janela_direita[polcompra-1] = 'x'
                total_vendido = total_vendido + 1
                
            elif opcao2 == 'je' or opcao2 == 'JE':
                if janela_esquerda == ['x', 'x' , 'x']:
                    print ('Todos os lugares estão ocupados!')
                    break
                print("Posicoes livres na janela:")
                for i in range(3):
                    if janela_esquerda[i] == 0:
                        print((i+1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                janela_esquerda[polcompra-1] = 'x' 
                total_vendido = total_vendido + 1
            else:
                print ('Opção invalida')
                
        elif opcao == "c" or opcao == "C":
            opcao3 = str(input('Corredor direito ou esquerdo? CD/CE: '))
            if opcao3 == 'cd' or opcao3 == 'CD':
                if corredor_direita == ['x', 'x' , 'x']:
                    print ('Todos os lugares estão ocupados!')
                    break
                for i in range(3):
                    if corredor_direita[i] == 0:
                        print((i+1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                corredor_direita[polcompra-1] = 'x'
                total_vendido = total_vendido + 1

            elif opcao3 == 'ce' or opcao3 == 'CE':
                if corredor_esquerda == ['x', 'x' , 'x']:
                    print ('Todos os lugares estão ocupados!')
                    break
                print("Posicoes livres no Corredor:")
                for i in range(3):
                    if corredor_esquerda[i] == 0:
                        print((i+1), end=" - ")
                polcompra = int(input("\nDigite o numero da poltrona desejada: "))
                corredor_esquerda[polcompra-1] = 'x'
                total_vendido = total_vendido + 1
            else:
                print ('Opção invalida')
                
        else:
            print ('Opção invalida')
            
        if total_vendido == 12:
            print ()
            print ('Todas as passagens foram vendidas')
            break
   
        comprar_2 = str(input('Deseja vender outra passagem? [S/N]: '))
        if comprar_2 == 's' or comprar_2 == 'S':
            limpar_tela()
            continue
        if comprar_2 == 'n' or comprar_2 == 'N':
            break
        
print ('  Bem vindo a venda de passagem!  ')
print()
while True:
    menu_passagem()
    escolha = int(input('Digite sua opção: '))
    if escolha == 1:
        vender_passagem()
    if escolha == 2:
        total_meia = pass_meia * 15
        total_inteira = pass_inteira * 30
        total_pass = total_meia + total_inteira
        print()
        print('O total de reais passagens é R$ {}'. format (total_pass))
        print ('O total vendido de bilhetes é {} unidades'. format (total_vendido))
        print ()
        if total_vendido < 5 : #pois com 6 vendidas ja completamos 50% dos lugares
            print ('Viagem cancelada, poucos bilhetes vendidos!')
            print()
            nova_venda = str(input('Deseja vender mais passagens? [S/N]: '))
            if nova_venda == 's':
                continue 
            else:
                print ('   --- Obrigada por utlizar nossos serviços! ---')
                break
        else:
            print('Viagem confirmada!')

    if escolha == 3:
        print ('    --- Obrigada por utlizar nossos serviços! ---')
        break
    if escolha == 4:
        poltronas()
        retornar = str(input ('Deseja retornar ao Menu? [S/N]:'))
        if retornar == 's':
            print ()
            continue
        else:
            print ('    --- Obrigada por utlizar nossos serviços! ---')
            break
            
input()
