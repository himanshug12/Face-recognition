import cv2

face_cascade=cv2.CascadeClassifier("C:\\Users\\Himanshu\\Desktop\\hd.xml")
eye_cascade=cv2.CascadeClassifier("C:\\Users\\Himanshu\\Desktop\\haarcascade_eye.xml")
cam=cv2.VideoCapture(0)
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_image=img[y:y+h,x:x+w]
        eye=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eye:
            cv2.rectangle(roi_image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
    cv2.imshow("img",img)
    k=cv2.waitkey(30) & 0xff
    if k == 27:
        break;
    
cam.release()
cv2.destroyAllWindows()       
            
            
