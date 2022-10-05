import cv2

video_capture = cv2.imread("C:/Users/claud/Downloads/PNG.jpg")
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


while True:

    faces = faceCascade.detectMultiScale(
        video_capture,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(video_capture, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow('video', video_capture)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()