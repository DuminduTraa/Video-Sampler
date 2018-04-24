import numpy as np
import cv2

time_interval = 5  # time interval between samples in seconds

cap = cv2.VideoCapture('input/test.mp4')
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
#print(fps)
count = 0
cap_count = 1
out_path = "/home/dumindu/Codes/Video-Sampler/output"

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True: 

        if count % (time_interval*fps) == 0 : 
            #print(count)
            cv2.imwrite("output/%d.jpg" % cap_count, frame)
            cap_count += 1 

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