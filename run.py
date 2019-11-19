"""Скрипт для тестирования алгоритма определения площади

    Фотографии в директории imgs/
    Примеры алгоритмов в algorithms/

    @author Alexandr Gorlov
"""

# Тестируемые фотографии
# "фото.jpg": площадь в пикселях
images = {
    "image01.jpg": 100,
    "image02.jpg": 107,
    "image03.jpg": 93,
    "image04.jpg": 200,
    "image05.jpg": 99,
    "image06.jpg": 102
}


import sys
import importlib
from datetime import datetime


try:
    algStr = sys.argv[1]
except IndexError:
    print("Прогон алгоритма определения площади на выборке фотографий.")
    print("Запуск: $ python3 run.py [алгоритм]")
    print("Пример: $ python3 run.py test - запустит алгоритм из test.py")
    print("Пример: $ python3 run.py test image01.jpg - запустит алгоритм из test.py, только для картинки image01.jpg")
    sys.exit(255)

try:
    alg = importlib.import_module("algorithms." + algStr)
except BaseException as err:
    serr = str(err)
    print("Ошибка: не удалось загрузить алгоритм='" + algStr + "': " + serr)
    sys.exit(255)

# Проверим алгоритм на одной фотографии
if len(sys.argv) == 3:
    try:
        imgSq = images[sys.argv[2]]
        images = {}
        images[sys.argv[2]] = imgSq
    except KeyError:
        print("Ошибка: фото ", sys.argv[2], " не найдено в списке images.")
        sys.exit(255)


print("Алгоритм: ", algStr)
print()

startTime = datetime.now()
testsCount = 0
okCount = 0

otkloneniePercent = 5

print("Площадь: фaктическая, px ~ ожидаемая, px; d- допустимое отклонение ({}%)".format(otkloneniePercent))
for image in images:
    testsCount += 1

    sq = alg.square(image)
    realSq = images[image]

    # Допустимое отклонение площади (сейчас 5%)
    otklonenie = int(realSq * (otkloneniePercent / 100))

    if ( abs(sq - realSq) < otklonenie ):
        okCount += 1
        print("{} OK! {} ~ {} (d={})".format(image, realSq, sq, otklonenie))
    else:
        print("{} FAIL! {} != {} (d={})".format(image, realSq, sq, otklonenie))

totaltime = datetime.now() - startTime

print("\nИтоговый счет: {} из {}. Время: {}".format(okCount, testsCount, totaltime))
