# AUTONOMOUS_DRIVING_WITH_TURTLEBOT3.
![150416328-160de66a-30b7-4a78-960b-b74db8ab4096](https://user-images.githubusercontent.com/62598684/203011017-f6f1d210-d519-4e8a-b8f4-f41636959439.jpeg)  ![Turtleninja](https://user-images.githubusercontent.com/62598684/203013394-dca774a6-542f-4eca-85a1-73550a111bdc.jpg) ![145659645-9ab35c4d-694e-499d-8fad-6bf1091d32ec](https://user-images.githubusercontent.com/62598684/203011326-ee9c67f2-d05e-4c54-91a4-aad4b3284b2e.jpeg)                                                        
                                                                                                                                                                                                                                                                                 
# Prepared By: SAMUEL IJEOMA BONIFACE & MISHECK EMMANUEL CHIRWA  
Supervised by: Duverne Raphael, Martins Renato, Rodriguez J. Joaquin.

![turtlebot3_burger_assembley_all_complete-thumb-480x640-5378](https://user-images.githubusercontent.com/62598684/203017851-24eb6de3-eaed-4965-8e4a-9be239f40ee9.jpg)

# PROBLEM_STATEMENT.
Our project focuses on turtlebot3 self-driving, that will take place on a race_track, with the detection on its yellow and white lines. Our main objective is to solve the autonomous driving lane tracking challenge, with all its phases properly explained on the Turtlebot3 E-Manual Robotics website.

# REQUIREMENTS.
TurtleBot3 is a new generation mobile robot that's modular, compact and customizable. Let's explore ROS and create exciting applications for education, research and product development. Below are the specs of our Turtlebot-3 Burger :  ![Burger_2](https://user-images.githubusercontent.com/62598684/203025095-a08caa99-d04c-4613-8ac2-5ff8434ddb73.jpg)  
- A stationed pc system is what we used which runs on linux ubuntu 20.04 which communicates with a single board computer (SBC) on turtlebot3 and it has to have ROS installed.

- Raspberry Pi ‘fish-eye’ camera.

- We will need ROS-Autorace-2020 packages and its dependances which can be found on ROBOTIS_GIT/autorace.

# Architecture
- Camera Calibration:
  - Camera Imaging Calibration
  - Intrinsic Camera Calibration
  - Extrinsic Camera Calibration
- Lane Detection.

# 1. Camera Calibration 
Geometric camera calibration estimates the parameters of a lens and image sensor of an image or video camera. These parameters could be used to correct lens distortion, measure the size of an object in world units, or determine the location of the camera in the scene.
Therefore, the camera mounted on our turtlebot3 is Raspberry Pi ‘fish-eye’ camera, thus, it has very large distortion. But the images needed for this project should have little distortion so as not to affect the image processing steps. To achieve this, we followed the description to run the **commands** from [Turtlebot3 E-Manual Robotics](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/) for the  **Camera Imaging Calibration**, **Intrinsic Camera Calibration** and **Extrinsic Camera Calibration**. 

   ## 1. (i) Camera Imaging Calibration
The camera imaging calibration was done by executing the **rqt_reconfigure** to modify the camera parameter values and enable the turtlebot3 mounted camera to see clear images as such, the contrast, brightness, sharpness, and saturation parameters for clarity of the system camera.
Thus, the modified parameters were overwritten in the **camera.yaml** file located in **turtlebot3autorace/calibration/camera_calibration** folder. This will make the camera set its parameters for the next launch. Here is the result of the modified image: ![WhatsApp Image 2022-11-21 at 1 35 17 PM](https://user-images.githubusercontent.com/62598684/203043626-717c524a-c45b-4729-b5a0-6a3a9e0ba798.jpeg)

 ## 1. (ii) Intrinsic Camera Calibration
The Intrinsic parameters of a camera deals with the camera's internal characteristics like its focal length, skew, distortion, and image center. For this project, the intrinsic calibration was done using a **6x8** printed checkerboard. The checkerboard was moved vertically on the x axis and horizontally on the y axis, well oriented in different directions for the skew and was moved farther and closer for the size. The GUI variables turn green after getting enough translation and orientation which as such means it's ready to be calibrated. ![WhatsApp Image 2022-11-21 at 1 36 31 PM](https://user-images.githubusercontent.com/62598684/203047192-6c675584-ee9a-4d25-8f9e-8953a17aa961.jpeg) ![Intrinsic Calibration](https://user-images.githubusercontent.com/62598684/203048000-59c126e8-8786-4b6a-9c15-58f04899ab2b.jpeg)

 After the calibration, the **calibrationdata.tar.gz** folder was created at /tmp folder. We then extract the data from the ost.yalm file and save it in **turtlebot3_autorace_camera/calibration/intrinsic_calibration/camerav2_320x240_30fps.yaml**. The result is shown below: ![Intrinsic parameters](https://user-images.githubusercontent.com/62598684/203049391-324b0f7f-eaab-4074-8a43-0b793ccd300a.jpeg)

## 1. (iii) Extrinsic Camera Calibration
The Extrinsic Camera calibration was done in order to acquire the robot pose and orientation. To get these done, we launched the intrinsic modified calibration parameters as such in **action mode** before running the Extrinsic calibration packages. The Extrinsic Camera Calibration launch file basically runs two source code **image_compensation.py** and **image_projection.py**. It then published **/camera/image_extrinsic_calib/compressed** which is the default image showing the unaligned red border according to 4 image coordinates and **/camera/image_projected_compensated** “birds-eye view” image showing the scale of the image brightness contrast of the compressed image according to the **clip_hist_percent** parameter defined after running the **rqt**. The images below shows the **default image** and **compensated image**: 
