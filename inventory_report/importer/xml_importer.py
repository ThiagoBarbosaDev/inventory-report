from inventory_report.importer.importer import Importer
# from importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @staticmethod
    def validate_path(path):
        if not path.endswith(".xml"):
            raise ValueError

    @staticmethod
    def import_data(path):
        try:
            XmlImporter.validate_path(path)
            data = []
            tree = ET.parse(path)
            root = tree.getroot()
            for record in root.findall("record"):
                item = {}
                for header in record:
                    item[header.tag] = header.text
                data.append(item)
            return data
        except ValueError:
            raise ValueError('Arquivo inválido')


# print(XmlImporter.import_data('inventory_report/data/inventory.xml'))
