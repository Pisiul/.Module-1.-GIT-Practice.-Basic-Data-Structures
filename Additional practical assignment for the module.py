#
# # ********************************************** Домашнее задание ************************************************** #
# # *************************************** ( "Базовые структуры данных." )******************************************* #
#
#                     Дополнительное практическое задание по модулю: "Базовые структуры данных."
#
# Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности
#
# Задание "Средний балл":
#
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать
# вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
#
# На вход даны следующие данные:
#
#     Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#     Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
#
#     Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#
# Например: 'Aaron' - [5, 3, 3, 5, 4]
#
#     Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
#
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
# ---------------------------------------------------------------------------------------

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ('Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron')
print(grades[0])
print(grades[1])
print(grades[2])
print(grades[3])
print(grades[4])

print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])

res = sorted(students)
students = (sorted(res))
print(res)
average_students = {}  # - Помните, что множество не является упорядоченной последовательностью.
# (нужен перевод в другой тип). Может я конечно просмотрел, но не помню такого способа на уроках.
# помог вопрос коллеги
average_students. update({students[0]: round(sum(grades[0]) / len(grades[0]), 2),
                          students[1]: round(sum(grades[1]) / len(grades[1]), 2),
                          students[2]: round(sum(grades[2]) / len(grades[2]), 2),
                          students[3]: round(sum(grades[3]) / len(grades[3]), 2),
                          students[4]: round(sum(grades[4]) / len(grades[4]), 2)})
print(average_students)
# -------------------------------------------------------------------------------------------------------------------- #
# D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe "D:\Программы\ProjectPyton\Module 1.
# GIT Practice. Basic Data Structures\Additional practical assignment for the module.py"
# [5, 3, 3, 5, 4]
# [2, 2, 2, 3]
# [4, 5, 5, 2]
# [4, 4, 3]
# [5, 5, 5, 4, 5]
# Johnny
# Bilbo
# Steve
# Khendrik
# Aaron
# ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.67, 'Steve': 4.8}
#
# Process finished with exit code 0
