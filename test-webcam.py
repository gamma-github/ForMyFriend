import cv2

cap = cv2.VideoCapture(0)

while True:
        ret, frame = cap.read()
#show frame

        cv2.imshow('camera capture', frame)

#10msec wait for typing key
        k = cv2.waitKey(10)
#ESCで終了
        if k == 27:
                break


cap.release()
cv2.destroyAllWindows()
