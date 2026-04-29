def multa(m):
    v = m * 4
    return v


pesca = float(input('Digite a quantidade pescada, em Kg: '))

if pesca > 100:
    excedente = pesca - 100
    mta = multa(excedente)
    print(f'O excedente é de: {excedente} Kg.')
    print(f'A multa a ser paga é de: R$ {mta}')

else:
    print('Não há excedente de pesca.')
    print('Não há multa a ser paga.')




