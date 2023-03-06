from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def load_data(self, path):
        self.data = [*self.data, *self.importer.import_data(path)]

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

    def import_data(self, path, report_type):
        self.load_data(path)
        response = InventoryRefactor.handle_report_type(report_type, self.data)
        return response
