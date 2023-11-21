# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
def create_snowflake_params(n):
    snow = []
    for _ in range(n):
        x = random.randint(0, 1200)
        y = random.randint(400, 600)
        length = random.randint(20, 50)
        snow.append({'x': x, 'y': y, 'length': length})
    return snow

def draw_snowflake(snows, color):
    for snowflake in snows:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point, length=snowflake['length'], color=color)

def moue_snow(snows):
    for snowflake in snows:
        if snowflake['y'] > 10:
            snowflake['x'] += random.randint(-10, 10)
            snowflake['y'] += random.randint(-30, 0)

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

N=20
snow = create_snowflake_params(n=N)


while True:
    sd.rectangle(sd.get_point(0, 0), sd.get_point(1200, 600), color=sd.background_color, width=0)
    draw_snowflake(snows=snow, color=sd.COLOR_WHITE)
    moue_snow(snows=snow)
    sd.sleep(0.05)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
