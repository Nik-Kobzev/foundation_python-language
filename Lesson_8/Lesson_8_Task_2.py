class Division:

    def division(self, d, a):
        try:
            result = d / a
        except ZeroDivisionError:
            result = "происходит деление на нолю "
        return result


print(Division().division(6, 6))
