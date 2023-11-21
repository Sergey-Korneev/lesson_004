# -*- coding: utf-8 -*-
import random

import simple_draw as sd
sd.resolution = (1200, 900)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


def draw_bunches(point, angle, lenght):
    if lenght < 10:
        return
    vector = sd.get_vector(start_point=point, angle=angle, length=lenght)
    vector.draw()
    next_point = vector.end_point
    next_angle0 = angle - random.randint(5, 30)
    next_angle1 = angle + random.randint(5, 30)
    next_lenght = lenght * random.uniform(0.75, 0.9)
    draw_bunches(point=next_point, angle=next_angle0, lenght=next_lenght)
    draw_bunches(point=next_point, angle=next_angle1, lenght=next_lenght)





# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)
# def draw_bunches(point, angle, lenght):
#     if lenght > 10:
#         vector = sd.get_vector(start_point=point, angle=angle, length=lenght)
#         vector.draw()
#         draw_bunches(point=vector.end_point, angle=angle + 30, lenght=lenght * .85)
#         draw_bunches(point=vector.end_point, angle=angle - 30, lenght=lenght * .85)
#
#     else:
#         return None

draw_bunches(sd.get_point(400,0), 90, 120)
# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


