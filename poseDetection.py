import cv2
import mediapipe as mp
import math
import numpy as np


def asciiArt():
    # make a cool ASCII graphic later -- those are cool
    print("INSERT ASCII HERE")

# add frame rate later


def cameraOpen():

    # mediapipe api handles pose detection
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    # log start of program;
    print("Starting Camera")
    # open webcam for parsing video
    cap = cv2.VideoCapture(0)

    # while(True):
    #     ret, frame = cap.read()

    #     grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #     thresh, blackAndWhiteFrame = cv2.threshold(
    #         grayFrame, 127, 255, cv2.THRESH_BINARY)

    #     cv2.imshow('video bw', blackAndWhiteFrame)
    #     #comment me out if you only want to see black and white
    #     cv2.imshow('video original', frame)

    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose_solution:

        maxTry = 10
        attempt = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("CAMMERA FAILED TO OPEN")
                if (attempt == maxTry):
                    break
                else:
                    attempt += 1
                    continue

            # pass in refrence no need to draw or return
            frame.flags.writeable = False
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose_solution.process(frame)

                # post processs results
            frame.flags.writeable = True
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
            )

            cv2.imshow('video', frame)

            #exit clause    
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cap.destroyAllWindows()


def main():
    asciiArt()
    cameraOpen()


if __name__ == '__main__':
    main()
