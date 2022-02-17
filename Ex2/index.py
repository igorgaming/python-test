class ListWorker:
    def __init__(self, *args):
        self.data = args

    def only_numbers(self):
        return [*filter(lambda item: isinstance(item, int), self.data)]

    def only_strings(self):
        return [*filter(lambda item: isinstance(item, str), self.data)]

    def except_numbers_strings(self):
        return [*filter(lambda item: not isinstance(item, str) and not isinstance(item, int), self.data)]

worker = ListWorker(1, 5, "test", 10, "test2", (5, 10), [10, 15, "test"])

print("Only numbers: ", worker.only_numbers())
print("Only strings: ", worker.only_strings())
print("Other objects: ", worker.except_numbers_strings())
