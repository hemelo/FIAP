# Nome: Henrique Fernandes de Castro Melo
# RM: 99397

DIAS_ANO = 30 * 12

def get_response_by_value(value):
    response = "Com o valor R$ {value:.2f}, você poderia ter "

    if value < 20000:
        response += "dado entrada em um carro."
    elif 20000 <= value <= 50000:
        response += "comprado um carro popular usado."
    else:
        response += "comprado um carro zero."

    return response.format(value=value)


def main():
    anos_fumante = float(input("Tempo como fumante (em anos).....: "))
    valor_maco = float(input("Valor do maço....................: "))
    quantia_dia = float(input("Quantidade de maços por dia......: "))

    total_gasto = valor_maco * quantia_dia * anos_fumante * DIAS_ANO
    print(get_response_by_value(total_gasto))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
