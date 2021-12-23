import math
import cv2
import numpy as np

def asciiArt():
    # make a cool ASCII graphic later -- those are cool
    print("INSERT ASCII HERE")

#add frame rate later
def cameraOpen():
    # log start of program;
    print("Starting Camera")
    # open webcam for parsing video
    cap = cv2.VideoCapture(0)


    while(True):
        ret, frame = cap.read()

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        thresh, blackAndWhiteFrame = cv2.threshold(
            grayFrame, 127, 255, cv2.THRESH_BINARY)

        cv2.imshow('video bw', blackAndWhiteFrame)

        #comment me out if you only want to see black and white
        cv2.imshow('video original', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cap.destroyAllWindows()


def main():
    asciiArt()
    cameraOpen()


if __name__ == '__main__':
    main()
