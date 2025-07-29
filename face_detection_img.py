import cv2, imutils;

haar = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


img0 =cv2.imread(r"C:\Users\santo\OneDrive\Pictures\Camera Roll\20231225_155531.jpg")
img = imutils.resize(img0, width =500)

while True:
    

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = haar.detectMultiScale(grayImg,1.3,4)

    for(x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),3)
    cv2.imshow("Window",img)

    key = cv2.waitKey(10)
    if(key == 27):
        break

cv2.destroyAllWindows()
