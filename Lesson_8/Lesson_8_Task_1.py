class Date:
    @classmethod
    def num_date(cls, date):

        d = []
        for i in date.split('-'):
            d.append(int(i))
        cls.validation_date(d)
        return d

    @staticmethod
    def validation_date(d):
        if d[0] > 31:
            raise ValueError('Число дня указанно больше 31')
        elif d[1] > 12:
            raise ValueError('Месяц не верно указан, больше 12')


print(Date.num_date('12-12-2013'))

