import numpy as np
import cv2

import argparse
 
parser = argparse.ArgumentParser(description="Video Sampler")
    
    
parser.add_argument("--input_vid", required=True, help="path to video")
parser.add_argument("--output_dir", required=True, help="output path")
parser.add_argument("--time", type=int, default=5, help="time interval between samples in seconds")

args = parser.parse_args()
print(args)

input_dir = args.input_dir
output_dir = args.output_dir
height = args.height
width = args.width

vid_file = args.input_vid
out_path = args.output_dir
time_interval = args.time  # time interval between samples in seconds

cap = cv2.VideoCapture(vid_file)
fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
#print(fps)
count = 0
cap_count = 1


while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if ret == True: 

        if count % (time_interval*fps) == 0 : 
            #print(count)
            cv2.imwrite(out_path + "/%d.jpg" % cap_count, frame)
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
