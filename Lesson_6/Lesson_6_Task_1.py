import time

class  TrafficLight:
    def __init__(self):
        self.__color = None
    def running(self,color):
        if color == 'green' and (self.__color == 'yellow' or self.__color == None) :
            print('GREEN')
            time.sleep(3)
            self.__color = color
        elif color == 'yellow' and (self.__color == 'red' or self.__color == 'green') :
            print('YELLOW')
            time.sleep(2)
            self.__color = color
        elif color == 'red' and (self.__color == 'yellow' or self.__color == None):
            print('RED')
            time.sleep(7)
            self.__color = color
        else:
            print('Порядок нарушен')

t = TrafficLight()
t.running('red')
t.running('red')
