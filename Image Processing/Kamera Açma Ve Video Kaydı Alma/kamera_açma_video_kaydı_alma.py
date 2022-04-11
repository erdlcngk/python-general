# -*- coding: utf-8 -*-
import cv2

# capture
cap = cv2.VideoCapture(0)

widht = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("genişlik: ", widht , " yükseklik: ", height)

writer = cv2.VideoWriter("video_kaydı.mp4",cv2.VideoWriter_fourcc(*"DIVX"),24,(widht,height))

while True:
    
    ret, frame = cap.read()
    cv2.imshow("Video",frame)
    
    # kaydetme
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
writer.release()
cv2.destoryAllWindows()