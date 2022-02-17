class Nikola:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age

        self._handle_name()

    def _handle_name(self):
        if self.name != "Николай":
            self.name = f"Я не {self.name}, я Николай"

nikola = Nikola("Николай", 18)
print(nikola.name)

nikola2 = Nikola("Максим", 23)
print(nikola2.name)
