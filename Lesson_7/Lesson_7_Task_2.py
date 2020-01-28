from abc import ABC, abstractmethod


class Coat:
    def __init__(self, size):
        self.size = size

    def material_coat(self):
        return self.size / 6.5 + 0.5

    @abstractmethod
    def dop_zadanie(self):
        pass


class Costume:
    def __init__(self, growth):
        self.growth = growth

    def material_costume(self):
        return 2 * self.growth + 0.3


class Clothes(Coat, Costume):
    def __init__(self, size, growth):
        # Coat.__init__(self, size)
        # Costume.__init__(self, growth)
        self.size = size
        self.growth = growth
        self._h = size # дополниткльное задание для property

    def sum_material(self):
        s = super().material_coat()
        d = super().material_costume()
        return s + d

    # дополниткльное задание для abstractmethod
    def dop_zadanie(self):
        pass

    @property
    def h(self):
        return self._h + 10


#
t = Clothes(10, 20)
print(t.sum_material())
print(t.h)
