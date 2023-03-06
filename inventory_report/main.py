import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def handle_importer(path):
    if path.endswith(".csv"):
        return CsvImporter
    elif path.endswith(".json"):
        return JsonImporter
    elif path.endswith(".xml"):
        return XmlImporter
    raise ValueError


def validate_args(last_arg):
    if last_arg is None:
        raise ValueError


def main():
    try:
        _, path, type_report = sys.argv
        validate_args(type_report)
        importer = handle_importer(path)
        inventory = InventoryRefactor(importer)
        print(inventory.import_data(path, type_report), end="")
    except ValueError:
        print("Verifique os argumentos", file=sys.stderr)
