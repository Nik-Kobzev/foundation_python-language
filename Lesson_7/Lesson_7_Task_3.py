class Cell:
    def __init__(self, count_cell):
        self.count_cell = count_cell

    def __add__(self, other):
        self.count_cell = self.count_cell + other.count_cell

    def __sub__(self, other):
        if self.count_cell - other.count_cell > 0:
            self.count_cell = self.count_cell - other.count_cell
        else:
            print('Разница меньше нуля')

    def __truediv__(self, other):
        self.count_cell = int(self.count_cell / other.count_cell)

    def __mul__(self, other):
        self.count_cell = self.count_cell * other.count_cell

    def make_order(self, cell, count_r):
        i = 1
        x = 1
        t = ''
        while i <= cell.count_cell // count_r:
            x = 1
            while x <= count_r:
                t = t + '*'
                x += 1
            t = t + '\\n'
            i += 1
        i = 1
        while i <= cell.count_cell % count_r:
            t = t + '*'
            i += 1
        return t


t1 = Cell(12)
t2 = Cell(10)
# t1 + t2
# t1 - t2
# t1 / t2
# t1 * t2
print(t1.make_order(t2, 4))
