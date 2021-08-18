
# >>> Mary=Employee("Mary","88888888",50000)
# >>> Mary
# <__main__.Employee object at 0x7f9a43686130>
# >>> Mary.print_salary_info()
# Employee Mary gets 50000 Rubles
# >>> Mary.phone
# '88888888'
# >>> import pickle
# >>> f = open('Mary_data', 'wb')
# >>> pickle.dump(Mary, f)
# >>> f.close()

#   Тут я перезашёл в REPL

# Mary
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'Mary' is not defined
# >>> import pickle
# >>> f = open('Mary_data', 'rb')
# >>> Mary=pickle.load(f)
# >>> f.close()
# >>> Mary.
# Mary.add(                Mary.name                Mary.print_salary_info(
# Mary.add_salary(         Mary.phone               Mary.salary
# >>> Mary.name
# 'Mary'
# >>> Mary.p
# Mary.phone               Mary.print_salary_info(
# >>> Mary.phone
# '88888888'
# >>> Mary.print_salary_info()
# Employee Mary gets 50000 Rubles
#--------------------------------------------------------------------------
# Модуль pickle реализует мощный алгоритм сериализации и десериализации объектов Python. 
# "Pickling" - процесс преобразования объекта Python в поток байтов, а "unpickling" - обратная операция, в результате которой поток байтов# преобразуется обратно в Python-объект.
# Плюсы:удобство использования, компактное сжатие.
# Минусы:безопасность, не защищен от ошибочных и вредоносных данных; ни в коем случае нельзя распаковывать файлы из ненадежных источников.
