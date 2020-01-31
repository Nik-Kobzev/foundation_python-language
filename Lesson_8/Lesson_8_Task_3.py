class My_list:
    def my_list(self, my_list_num):
        for i in my_list_num:
            f = float(i)

a = True
m_list =[]
while a:
    t = input('Ведите число списка, выход слово stop: ')
    if t == 'stop':
        break
    m_list.append(t)
    My_list().my_list(m_list)

print(m_list)