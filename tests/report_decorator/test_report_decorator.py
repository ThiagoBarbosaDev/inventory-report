from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    data = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-01-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 2,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 3,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Breezy Ltda",
            "data_de_fabricacao": "2022-02-04",
            "data_de_validade": "2023-05-04",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 4,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-03-02",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 5,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Bengal Co",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-03-02",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
        {
            "id": 6,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Bengal Co",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-03-02",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        },
    ]
    decoratedReport = ColoredReport(SimpleReport).generate(data)
    data_fabricacao = "\033[36m2022-02-04\033[0m"
    data_validade = "\033[36m2023-05-04\033[0m"
    empresa = "\033[31mForces of Nature\033[0m"
    assert decoratedReport == (
        f"\033[32mData de fabricação mais antiga:\033[0m {data_fabricacao}\n"
        f"\033[32mData de validade mais próxima:\033[0m {data_validade}\n"
        f"\033[32mEmpresa com mais produtos:\033[0m {empresa}"
    )
