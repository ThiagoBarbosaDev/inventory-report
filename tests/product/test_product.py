from inventory_report.inventory.product import Product

intrucoes = 'Manter fora do alcance de crianças e devs'


def test_cria_produto():
    product = Product(
        1,
        'Café da Trybe',
        'Trybe',
        '01/01/2023',
        '03/03/2023',
        '69420',
        intrucoes
    )
    print('##################')
    print(product.id)
    print(product.nome_da_empresa)
    assert product.id == 1
    assert product.nome_da_empresa == 'Trybe'
    assert product.nome_do_produto == 'Café da Trybe'
    assert product.data_de_fabricacao == '01/01/2023'
    assert product.data_de_validade == '03/03/2023'
    assert product.numero_de_serie == '69420'
    assert product.instrucoes_de_armazenamento == intrucoes
