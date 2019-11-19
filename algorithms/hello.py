"""Ознакомительная реализация

    Пример поиска границ заказа
    Автор: Alexandr Gorlov

"""
import cv2

def square(image) -> int:
    """Определим площадь, с помощью OpenCv.findContours"""

    image = cv2.imread("./imgs/" + image)

    # 0. вырежем центральную часть
    #image = image[100:1700, 350:2050]

    # 1. Переведем в градации серого
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. Немного размажем границы
    grayImage = cv2.GaussianBlur(grayImage, (51, 51), 0)

    viewImage(grayImage, "Перевел в градации серого и размыл")

    # 3. Переведем в черно-белое (если пиксель ярче 30 - считаем белым, если темнее - черным)
    ret, bwImage = cv2.threshold(grayImage, 30, 255, 0)

    viewImage(bwImage, "Перевел в черно-белое (без переходов)")

    # 4. Поищем контуры с помощью OpenCV.findContours
    _, contours, hierarchy = cv2.findContours( bwImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    maxConturArea = 0

    # 5. Выберем самый большой из них
    i = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > maxConturArea:
            maxConturArea = area
            maxContur = i

        i += 1

    cv2.drawContours( image, contours, maxContur, (0,0,255), 3, cv2.LINE_AA, hierarchy, 1 )
    viewImage(image, "Итоговый контур")

    return maxConturArea

def viewImage(image, nameOfWindow):
    """Вывод картинки для наладки

      ESC - закрывает окно
      кнопка s - сохраняет в файле tmp.png

    """

    # Чтобы выключить отладку, раскоментировать следующую строку:
    # return
    cv2.namedWindow(nameOfWindow, cv2.WINDOW_NORMAL)
    cv2.imshow(nameOfWindow, image)
    k = cv2.waitKey(0)

    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('tmp.png', image)
        cv2.destroyAllWindows()