def calcular_imposto(valor_produto):
    if valor_produto<100:
        return valor_produto*0.5
    elif valor_produto>=100:
        return valor_produto*0.10
def aplicar_cupom(valor_base,cupom):
    if cupom=="PROMO15":
        return valor_base*0.15
    elif cupom=="FESTA10":
        return valor_base*0.10
    else:
        return 0.0
def main():
    nome=input('Digite o nome do produto:').strip().lower()
    preço=float(input('Digite o valor do produto:'))
    cupom=input('Digite o cupom(se souber!)').upper()
    x=calcular_imposto(preço)
    y=aplicar_cupom(preço,cupom)
    conta_final=preço+x-y
    print(f'Nome do produto:{nome.capitalize()}')
    print(f'preço original R${preço:.2f} reais')
    print(f'Cupom: {cupom} desconto do cupom R${y:.2f} reais')
    print(f'imposto R${x}')
    print(f'Valor final R${conta_final:.2f}')
if __name__=='__main__':
    main()