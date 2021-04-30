import cv2
import numpy as np
import pyautogui
import time


# Sizing the screen
screen_size = (1920,1080) 

# Loading the Video Writer
output = cv2.VideoWriter("filename.avi" , cv2.VideoWriter_fourcc(*'XVID'), 10.0 , screen_size)

# Setting fps
fps = 120
prev = 0

# Main loop
while True:
    time_elapsed = time.time() - prev
    img = pyautogui.screenshot()
    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.putText(frame, "Recorder", (960, 70), cv2.FONT_HERSHEY_TRIPLEX, 1, (106, 90, 205), 2)
        output.write(frame)
    cv2.waitKey(100)
    
cv2.destroyAllWindows()
output.release()