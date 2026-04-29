def multa(m):
    v = m * VALOR_MULTA
    return v


VALOR_MULTA = 4.0
LIMITE = 100


pesca = float(input('Digite a quantidade pescada, em Kg: '))

if pesca > LIMITE:
    excedente = pesca - LIMITE
    vl_mta = multa(excedente)
    print(f'O excedente é de: {excedente} Kg.')
    print(f'A multa a ser paga é de: R$ {vl_mta}')

else:
    print('Não há excedente de pesca.')
    print('Não há multa a ser paga.')




