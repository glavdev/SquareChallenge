# SquareChallenge

SquareChallenge - определение площади заказа по фото

## Конкурс

Нужно Реализовать свою функцию ``square(image) -> int``,
которая будет подсчитывать площадь посылки на фотографии.

Подборка фотографий находится в каталоге **imgs**.

Выигрывает функция, которая даст наибольшее число верных
ответов. 

Результат подсчитывается скриптом ``run.py``.

При равных результатах выигрывает, та что затрачивает меньше времени.

Свою функцию поместить в каталог ``algorithms`` через пул-реквест.

Конкурс длится 2 недели (c 20.11.2019 по 4.12.2019).
Выполняется в свободное время.
Призовой фонд: 10000р.

## Подготовка проекта

1. Используем питон версии 3 ``python3``
2. устанавливаем библиотеку: ``OpenCV``: (ubuntu 18.04)
```sh
$ sudo apt install python3-opencv
```

3. Запуск:

Все фото функцией square из файла test.py
```sh
$ python3 run.py test
```

Одно фото:
```sh
$ python3 run.py test image01.jpg
```

## Для старта

Быстрое введение в Python:
https://www.raspberrypi.org/documentation/usage/python/

Введение в работу с изображениями с помощью OpenCV:
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

Шпаргалка по opencv:
https://tproger.ru/translations/opencv-python-guide/#antialiasing

Еще статья:
https://towardsdatascience.com/object-detection-via-color-based-image-segmentation-using-python-e9b7c72f0e11
