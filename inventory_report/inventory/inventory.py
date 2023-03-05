import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def read_data(path):
        data = []
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)

            data = list(reader)
        return data

    @staticmethod
    def handle_report_type(report_type, data):
        try:
            if report_type == "simples":
                return SimpleReport.generate(data)
            if report_type == "completo":
                return CompleteReport.generate(data)
            raise ValueError
        except ValueError:
            return ValueError('Unsupported type value')

    @staticmethod
    def import_data(path, report_type):
        print(path)
        data = Inventory.read_data(path)
        print(data)
        response = Inventory.handle_report_type(report_type, data)
        return response
