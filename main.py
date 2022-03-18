#load the cascade
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

#to capture video from webcam
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

#to use a video file as input
#cap=cv2.VideoCapture("filename.mp4")

while True:
   #read the frame
   ret,img=cap.read()
   #convert to grayscale
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   #detect the faces
   faces = face_cascade.detectMultiScale(gray,1.1,4)
   #draw the rectangle around each face
   for(x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   #display
   cv2.imshow('img',img)
   #stop if escape key is pressed
   k=cv2.waitKey(30) & 0xff
   if k==27:
      break
#release the video capture
cap.release()