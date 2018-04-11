import numpy as np
import cv2

time_interval = 5

cap = cv2.VideoCapture("test.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
#print(fps)
count = 0

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True: 

        if count % (time_interval*fps) == 0 : 
            print(count)
            #cv2.imwrite("frame%d.jpg" % count, frame)

        # Display the resulting frame
        cv2.imshow('frame',frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        count += 1 
        
    else: 
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()