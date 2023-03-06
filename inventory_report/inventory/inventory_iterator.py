from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __next__(self):
        try:
            return self.data[self.index]
        except IndexError:
            raise StopIteration
        finally:
            self.index += 1
