import numpy as np
import cv2
import matplotlib.pyplot as plt


def detect_eyes(img):
    face_img = img.copy()

    eyes = eye_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in eyes:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 2)

    return face_img


def live_detection_by_camera():
    cap = cv2.VideoCapture(0)

    while True:

        ret, frame = cap.read(0)

        frame = detect_eyes(frame)

        cv2.imshow('Video Face Detection', frame)

        c = cv2.waitKey(1)
        # Esc key
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


einstein = cv2.imread('../data/albert_einstein.jpg', 0)

eye_cascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')

plt.imshow(einstein, cmap='gray')
plt.show()

result = detect_eyes(einstein)
plt.imshow(result, cmap='gray')
plt.show()

live_detection_by_camera()