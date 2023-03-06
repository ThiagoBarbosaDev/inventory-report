from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def validate_path(path):
        if not path.endswith(".csv"):
            raise ValueError

    @staticmethod
    def import_data(path):
        try:
            CsvImporter.validate_path(path)
            with open(path) as csv_file:
                reader = csv.DictReader(csv_file)
                return list(reader)
        except ValueError:
            raise ValueError('Arquivo inválido')
