import cv2
import numpy as np
import os
def main():

    capWebcam = cv2.VideoCapture(0)
    capWebcam.set(cv2.CAP_PROP_FRAME_WIDTH, 320.0)   
    capWebcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240.0)
    
    if capWebcam.isOpened() == False:             
        print "error: camer-iig neej chadsangui \n\n"      
        os.system("pause")                                         
        return                                 

    while cv2.waitKey(1) != 27 and capWebcam.isOpened():         
        blnFrameReadSuccessfully, imgOriginal = capWebcam.read()
        if not blnFrameReadSuccessfully or imgOriginal is None:    
            print "aldaa: camer-g neej chadsangui\n"             
            os.system("pause")                                      
            break                                       
        imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)    
        imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)        
        imgCanny = cv2.Canny(imgBlurred, 100, 200)                 
        cv2.imshow("undsen", imgOriginal)         
        cv2.imshow("Canny", imgCanny)

    cv2.destroyAllWindows()                 
    return

if __name__ == "__main__":
    main()

