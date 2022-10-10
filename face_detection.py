#from tkinter import Frame
# Import OpenCV Libraries
import cv2


# Import Haar Cascade Classifier for face and eye detection
face_hcascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_hcascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#eyeglasses_hcascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)                   # Convert camera to gray
    faces =  face_hcascade.detectMultiScale(gray, 1.3, 5)           # Detect the face and keep the position

    for (x, y, w, h) in faces:                                      # Frames position (width=x, height=y)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)  
        face_gray = gray[y:y+h, x:x+w]                              
        face_clr = frame[y:y+h, x:x+w]

        eyes = eye_hcascade.detectMultiScale(face_gray)
        #eyeglasses = eyeglasses_hcascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_clr, (ex, ey), (ex+ew, ey+eh), (0, 127, 255), 2)
        
        #for (gx, gy, gw, gh) in eyeglasses:
            #cv2.rectangle(face_clr, (gx, gy), (gx+gw, gy+gh), (0, 127, 255), 2)

    cv2.imshow('Image', frame)                  # Show the video
    if cv2.waitKey(1) & 0xFF == ord('q'):       # Quit face detection video using q
        break

    #if k == 10:
        #break

cap.release()
cv2.destroyAllWindow()