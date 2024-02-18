import cv2

import time


webCam = cv2.VideoCapture(0)
currentframe = 0


while (True):
    success, frame = webCam.read()
    cv2.imshow("Output", frame)
    Image= cv2.imwrite("frame" + str(currentframe)+".jpg", frame)
    print(Image)
    currentframe +=1
    
    # Wait for 10 seconds
    time.sleep(10)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
    

webCam.release()
cv2.destroyAllWindows()