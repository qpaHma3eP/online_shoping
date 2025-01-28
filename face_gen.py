import cv2
import os


# Получаем доступ к папке со скриптом
path = os.path.dirname(os.path.abspath(__file__))
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
i = 0
offset = 50
name = input('Введите id пользователя: ')
video = cv2.VideoCapture(0)


while True:
    ret, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        i += 1
        cv2.imwrite('dataSet/face-'+name+'.'+str(i)+'.jpg', gray[y-offset:y+h+offset, x-offset:x+w+offset])
        cv2.waitKey(100)
    if i>30:
        video.release()
        cv2.destroyAllWindows()
        break

