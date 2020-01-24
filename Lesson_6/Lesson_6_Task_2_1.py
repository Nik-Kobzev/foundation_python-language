class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight(self):
        return self.__length * self.__width * 25 * 5/1000


t = Road(20, 5000)
print(f'{t.weight()} тон')
