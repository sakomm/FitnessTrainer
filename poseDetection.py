import cv2
import mediapipe as mp
import math

def asciiArt():
    # make a cool ASCII graphic later -- those are cool
    print("       _             _    ")
    print("      | |           | |   ")
    print(" _ __ | | __ _ _ __ | | __")
    print("| '_ \| |/ _` | '_ \| |/ /")
    print("| |_) | | (_| | | | |   < ")
    print("| .__/|_|\__,_|_| |_|_|\_\\")
    print("| |                       ")
    print("|_|                       ")
   
def cameraOpen():
    # mediapipe api handles pose detection
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    # log start of program;
    print("Starting Camera")
    # open webcam for parsing video
    cap = cv2.VideoCapture(0)


    with mp_pose.Pose(
        #dropping down the confidence threshold to 0.25 from .5 to make more data
        # if causing errors due to inacuracy raise confidence threshold
        min_detection_confidence=0.25,
        min_tracking_confidence=0.5,
        model_complexity=2
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

            #plot 3d results
            
            #  only returns a static image until the next frame is processed and figure is closed 
            # plotGenerator.plot_landmarks_animated(results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                      
            # display results
            cv2.imshow("POSE-DETECTOR-INATOR", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
    cap.release()
    cap.destroyAllWindows()

def angleCalc(landmarkA, landmarkB, landmarkC):

    # get the x and y coordinates of the landmarks
    xA, yA ,zA= landmarkA
    xB, yB ,zB= landmarkB
    xC, yC ,zC= landmarkC

    # use the theta cosine rule to find the angle between the two vectors
    # theta = acos((a^2 + b^2 - c^2)/(2ab))
    angle = math.degrees(math.atan2(yC - yB, xC - xB) - math.atan2(yA - yB, xA - xB))

    return angle



def main():
    asciiArt()
    angleTest = angleCalc((558, 326, 0), (642, 333, 0), (718, 321, 0))
    print(f'The calculated angle is {angleTest}')
    cameraOpen()


if __name__ == '__main__':
    main()
