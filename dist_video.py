import math
import cv2
from pygame import mixer

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # loading files
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mixer.init()
mixer.music.load('a.mpeg')
mixer.music.set_volume(0.02)

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('v.mp4')
while True:
    ret, image1 = cap.read(0)
    image = cv2.resize(image1, (800, 600))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))

    l = []
    l1 = []
    lf = []

    i = 1


    for (x, y, w, h) in faces:
        # cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        s = str(i)  # Face No.
        i += 1
        l.append(x)
        l.append(y)
        print(l)

    for (x, y, w, h) in faces:
        l1.append(w)

        l1.append(h)

        print(l1)

    a = len(l)//2
    # print(a)
    j = 2
    for i in range(1, a):
        d = math.sqrt(((l[0] - l[j]) ** 2) + ((l[1] - l[j + 1]) ** 2))
        print(d)
        # print(j)
        cv2.putText(image, 'REFERENCE', (l[0], l[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        cv2.rectangle(image, (l[0], l[1]), (l[0] + l1[0], l[1] + l1[1]), (0, 255, 255), 2)
        if (d > 550):
        # if (d > 450):
            print('following')
            cv2.putText(image, 'FOLLOWING', (l[j], l[j + 1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.rectangle(image, (l[j], l[j + 1]), (l[j] + l1[j - 2], l[j + 1] + l1[j - 1]), (0, 255, 0), 2)
        else:
            print('not following')
            cv2.putText(image, 'NOT FOLLOWING', (l[j], l[j + 1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.rectangle(image, (l[j], l[j + 1]), (l[j] + l1[j - 2], l[j + 1] + l1[j - 1]), (0, 0, 255), 2)
            mixer.music.play()

        j += 2

    cv2.namedWindow('Social', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Social', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Social", image)

    k = cv2.waitKey(1)
    if (k == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()