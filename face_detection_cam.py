import cv2

haar = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam =cv2.VideoCapture(0)

while True:

    _,img = cam.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = haar.detectMultiScale(grayImg,1.3,4)

    for(x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),3)
    cv2.imshow("Window",img)

    key = cv2.waitKey(10)
    if(key == 27):
        break
cam.release()
cv2.destroyAllWindows()
