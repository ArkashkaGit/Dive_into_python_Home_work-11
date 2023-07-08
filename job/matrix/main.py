# Создайте класс Матрица. Добавьте методы для:
# вывода на печать
# сложения
# сравнения


from class_matrix import *

# Создаю два экземпляра класса матриц с указанием размеров
first_matrix = Matrix(5, 5)
second_matrix = Matrix(5, 5)

# Задаю рандомные значения в матрицы
first_matrix.to_create_matrix()
second_matrix.to_create_matrix()

# Складываю две матрицы
new_matrix = first_matrix.summa_matrix(second_matrix.matrix)

# вывожу новую матрицу на экран
print_matrix(new_matrix)

first_matrix.__str__()
second_matrix.__str__()

first_matrix.__repr__()
second_matrix.__repr__()

# вывожу на экран сумму элементов матриц
print('Сумма элементов первой матрицы =', first_matrix.summ_element_matrix)
print('Сумма элементов второй матрицы =', second_matrix.summ_element_matrix)

# Вывожу на экран сравнение двух матриц
print(first_matrix == second_matrix)
print(first_matrix != second_matrix)
print(first_matrix > second_matrix)
print(first_matrix >= second_matrix)
print(first_matrix < second_matrix)
print(first_matrix <= second_matrix)

# вывд документации в терминал
help(Matrix)