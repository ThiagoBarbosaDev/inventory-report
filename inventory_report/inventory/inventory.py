import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def read_csv(path):
        with open(path) as csv_file:
            reader = csv.DictReader(csv_file)
            return list(reader)

    @staticmethod
    def read_json(path):
        with open(path) as json_file:
            content = json_file.read()
            return json.loads(content)

    @staticmethod
    def read_xml(path):
        data = []
        tree = ET.parse(path)
        root = tree.getroot()
        for record in root.findall("record"):
            item = {}
            for header in record:
                print(header)
                item[header.tag] = header.text
            data.append(item)
        return data

    @staticmethod
    def read_data(path):
        data = []
        if path.endswith(".csv"):
            data = Inventory.read_csv(path)
        elif path.endswith(".json"):
            data = Inventory.read_json(path)
        elif path.endswith(".xml"):
            data = Inventory.read_xml(path)
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
