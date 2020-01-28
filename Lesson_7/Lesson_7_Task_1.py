class Matrix:
    def __init__(self, List):
        l = []
        for i in List:
            l.append(len(i))
        if len(set(l)) > 1:
            raise ValueError("Размерность матрици не соотвктствует n на m")
        self.matrix = List

    def __str__(self):
        r = ''
        for i in self.matrix:
            r = r + str(i) + '\n'
        return f'{r}'

    def __add__(self, other):
        i = 0
        while i < len(self.matrix):
            y = 0
            while y < len(self.matrix[i]):
                self.matrix[i][y] = self.matrix[i][y] + other[i][y]
                y += 1
            i += 1

my_matrix = Matrix([[1, 2, 3], [3, 5, 6]])
print(my_matrix)
my_matrix + [[1, 2, 3], [3, 5, 6]]
print('сумма матриц')
print(my_matrix)