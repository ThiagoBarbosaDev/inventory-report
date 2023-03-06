from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        4,
        "Café da Trybe",
        "Trybe",
        "2022-01-01",
        "2022-04-04",
        "69420",
        "em local seco",
    )

    expected = (
        "O produto Café da Trybe fabricado em 2022-01-01 por Trybe com "
        "validade até 2022-04-04 precisa ser armazenado em local seco."
        )
    assert str(product) == expected
