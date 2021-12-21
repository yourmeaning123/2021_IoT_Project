import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

face_cascade = cv2.CascadeClassifier('./xml/face.xml')



while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if not ret:
        break
    
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    if cv2.waitKey(10) == 27:
        break
    
    cv2.imshow('frame1', frame)

cap.release()
cv2.destroyALLWindows()