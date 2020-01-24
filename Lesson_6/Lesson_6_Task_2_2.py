class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income
        self._r=self.__income


class Position(Worker):
    def __init__(self,name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._r['wage'] + self._r['bonus']


t = Position('Viktot', 'Popov', 'ingener', {'wage': 40, 'bonus': 60})
print(t.get_full_name())
print(t.get_total_income())

# t = {'wage':40, 'bonus': 60}
# print(type(t))
