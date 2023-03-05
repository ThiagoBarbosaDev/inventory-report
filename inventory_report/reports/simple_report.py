from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def find_oldest(data):
        oldest_date = min([item["data_de_fabricacao"] for item in data])
        return oldest_date

    @staticmethod
    def find_closest(data):
        closest_date = max([item["validade"] for item in data])
        return closest_date

    @staticmethod
    def find_closest_to_today(data):
        today = datetime.now().date()
        closest_date = min(
            [
                datetime.strptime(item["data_de_validade"], "%Y-%m-%d").date()
                for item in data
                if datetime.strptime(
                    item["data_de_validade"], "%Y-%m-%d"
                ).date()
                >= today
            ]
        )
        return closest_date.strftime("%Y-%m-%d")

    @staticmethod
    def find_most_common(data):
        companies = [item["nome_da_empresa"] for item in data]
        company_counter = Counter(companies)
        most_common = company_counter.most_common(1)[0][0]
        return most_common

    @staticmethod
    def generate(data):
        oldest = SimpleReport.find_oldest(data)
        closest = SimpleReport.find_closest_to_today(data)
        most_common = SimpleReport.find_most_common(data)
        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com mais produtos: {most_common}"
        )
