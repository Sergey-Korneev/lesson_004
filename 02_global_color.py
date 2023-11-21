# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def draw_figur(point, angle, length, count_start, count_end, color):
    if count_start < count_end:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length)
        v1.draw(color=color)
        count_start += 1
        angle += 360/count_end
        draw_figur(point=v1.end_point, angle=angle, length=length,
                   count_start=count_start, count_end=count_end, color=color)
    elif count_start > count_end:
        return None


draw_figur(point=sd.get_point(50, 50), angle=0, length=100, count_start=0, count_end=3, color=sd.COLOR_RED)

sd.pause()
