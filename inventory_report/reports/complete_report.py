# from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    # def __init__(self, data):
    #     self.data = data

    @staticmethod
    def count_company_products(data):
        products_counter = Counter(item["nome_da_empresa"] for item in data)
        return products_counter.most_common()

    @staticmethod
    def create_company_ocurrency(data):
        company_ocurrency = ""
        for company, quantity in data:
            company_ocurrency += f"- {company}: {quantity}\n"
        return company_ocurrency

    @staticmethod
    def generate(data):
        oldest = CompleteReport.find_oldest(data)
        closest = CompleteReport.find_closest_to_today(data)
        most_common = CompleteReport.find_most_common(data)
        products = CompleteReport.count_company_products(data)
        company_ocurrency = CompleteReport.create_company_ocurrency(products)
        simple_report = (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com mais produtos: {most_common}\n"
            "Produtos estocados por empresa:\n"
        )
        return simple_report + company_ocurrency


# data = [
#     {
#         "id": 1,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-01-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Pinto",
#         "data_de_fabricacao": "2022-02-04",
#         "data_de_validade": "2023-05-04",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-03-02",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Benga Co",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-03-02",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
#     {
#         "id": 4,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Benga Co",
#         "data_de_fabricacao": "2022-04-04",
#         "data_de_validade": "2023-03-02",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar em local fresco",
#     },
# ]


# print(CompleteReport.generate(data))
