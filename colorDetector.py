import cv2
import numpy as np

webcam = cv2.VideoCapture(0)

HSV_value_color = [
    ((0, 100, 100), (10, 255, 255), 'red'),
    ((35, 50, 50), (85, 255, 255),  'green'),
    ((100, 70, 70), (130, 255, 255), 'blue'),
]

color_values = {"blue": (255, 0, 0),
                "red": (0, 0, 255),
                "green": (0, 255, 0)
                }

while True:

    _, frame = webcam.read()

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for lower, upper, color in HSV_value_color:

        mask = cv2.inRange(img_hsv, np.array(lower), np.array(upper))

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 440:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y), (x+w, y+h), color_values[color], 2)
                cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_TRIPLEX, 0.5, color_values[color], 1)

#        cv2.imshow(f"mask {color}", mask)
    cv2.imshow("Color Detection", frame)

    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()


