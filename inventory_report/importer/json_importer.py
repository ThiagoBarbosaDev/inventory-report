from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def validate_path(path):
        if not path.endswith(".json"):
            raise ValueError

    @staticmethod
    def import_data(path):
        try:
            JsonImporter.validate_path(path)
            with open(path) as json_file:
                content = json_file.read()
            return json.loads(content)
        except ValueError:
            raise ValueError('Arquivo inválido')


# print(JsonImporter.import_data('inventory_report/data/inventory.csv'))
