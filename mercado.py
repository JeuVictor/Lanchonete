#Restaurante que te dá o falor total  das compras com descontos já aplicado.
#Desenvolvido por Jeú Victor em 17/05/2022.
print("*"*41)
print ('')
print ('............ Menu Restaurante ...........')
print ('')
print("*"*41)
print('Escolha qual produto gostaria de comprar?')
print("*"*41)
print('* Codigo  ---- Produto ----------- Preço*')
print('*001  -----Cachorro Quente ----- R$10,99*')
print('*002 ------Refrigerante -------- R$ 5,99*')
print('*003 ------pudim --------------- R$ 3,99*')
print('*004 ------Cancelar --------------------*')
print("*"*41)
codigo = int(input('Digite o Codigo do produto: '))

if codigo == 1:
   print("*"*41)
   qtd = int(input('Digite a quantidade: '))
   print("*"*41)
   valor = 10.99
   if qtd <= 5:
     desconto = valor*qtd*0.02
     total = valor*qtd - desconto
     print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
   else:
    if qtd >= 6 and qtd <= 10:
        desconto = valor*qtd*0.03
        total = valor*qtd - desconto
        print ('O Valor total da compr341452a é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
    else:
        desconto = valor*qtd*0.05
        total = valor*qtd - desconto
        print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
if codigo == 2:
   valor = 5.99
   print("*"*41)
   qtd = int(input('Digite a quantidade: '))
   print("*"*41)
   if qtd <= 5:
    desconto = (valor*qtd)*0.02
    total = (valor*qtd) - desconto
    print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
   else:
    if qtd >= 6 and qtd <= 10:
        desconto = valor*qtd*0.03
        total = valor*qtd - desconto
        desconto = valor*qtd*0.03
        total = valor*qtd - desconto
        print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
    else:
        desconto = valor*qtd*0.05
        total = valor*qtd - desconto
        print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
if codigo == 3:
   valor = 3.99
   print("*"*41)
   qtd = int(input('Digite a quantidade: '))
   print("*"*41)
   if qtd <= 5:
    desconto = valor*qtd*0.02
    total = valor*qtd - desconto
    print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
   else:
    if qtd >= 6 and qtd <= 10:
        desconto = valor*qtd*0.03
        total = valor*qtd - desconto
        desconto = valor*qtd*0.03
        total = valor*qtd - desconto
        print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
    else:
        desconto = valor*qtd*0.05
        total = valor*qtd - desconto
        print ('O Valor total da compra é R${:.2f} com o desconto recebido de R${:.2f}.'.format(total, desconto))
else:
   print("*"*41)
   print('Obrigado pela preferencia! Volte sempre')
   print("*"*41)
print("*"*41)
