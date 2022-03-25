# FitnessTrainer
Track human body movement to test if they have proper form when doing exercise and then provide feedback

to do this we will be using pose detection from openCV and track key points to determine weather or not the user is doing the exercise properly or not

we will provide feedback to the user based on the pose detection

to capture the user we will be using openCV and the webcam to capture the user at a specific time this can be done actively.



https://user-images.githubusercontent.com/55466413/160177109-78eaceee-dd2f-4e1c-94dc-b7e5e5112fbf.mp4



requirements:
- openCV2
- mediapipe
- tensorflow
- python

Goals:  
- Track key points -- Completed 12/23/21
- Detect pose (exercise we will be tracking is the plank)
- Determine if pose is correct
    - if pose is correct, then provide message to user
    - if pose is incorrect, then provide message to user
- Provide feedback  

