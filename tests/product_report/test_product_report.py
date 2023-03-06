from inventory_report.inventory.product import Product

product = Product(
    4,
    "Café da Trybe",
    "Trybe",
    "01/01/2022",
    "01/02/2022",
    "69420",
    "em local seco",
)

expected = "O produto Café da Trybe fabricado em 01/01/2022 por Trybe com \
validade até 01/02/2022 precisa ser armazenado em local seco."


def test_relatorio_produto():
    assert str(product) == expected
