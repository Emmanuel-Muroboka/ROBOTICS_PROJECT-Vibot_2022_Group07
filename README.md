# AUTONOMOUS_DRIVING_WITH_TURTLEBOT3.

<img align="left" width="200" height="100" src="https://user-images.githubusercontent.com/62597513/145659645-9ab35c4d-694e-499d-8fad-6bf1091d32ec.jpeg">
<img align="right" width="180" height="100" src="https://user-images.githubusercontent.com/62597513/150416328-160de66a-30b7-4a78-960b-b74db8ab4096.jpeg">
![Turtleninja](https://user-images.githubusercontent.com/62598684/206926255-e5ca22d3-f2d5-4282-839e-96df996d9cdd.jpg)
                                                                                                                                                                                                                                                                                 
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
The Extrinsic Camera calibration was done in order to acquire the robot pose and orientation. To get these done, we launched the intrinsic modified calibration parameters as such in **action mode** before running the Extrinsic calibration packages. The Extrinsic Camera Calibration launch file basically runs two source code **image_compensation.py** and **image_projection.py**. It then published **/camera/image_extrinsic_calib/compressed** which is the default image showing the unaligned red border according to 4 image coordinates and **/camera/image_projected_compensated** “birds-eye view” image showing the scale of the image brightness contrast of the compressed image according to the **clip_hist_percent** parameter defined after running the **rqt**. The images below shows the **default image** , **compensated image** and **rqt configuration_parameters**: ![Extrinsic Calibration](https://user-images.githubusercontent.com/62598684/203057320-48216c17-e5dc-430f-9b8a-79f3618fd9fa.jpeg)

We excuted rqt_reconfigure to adjust the parameters and the modifed parameters are saved in **turtlebot3_autorace_camera/calibration/extrinsic_calibration/projection.yaml** and **turtlebot3_autorace_camera/calibration/extrinsic_calibration/compensation.yaml** files.
![Extrinsic Parameters Configuration](https://user-images.githubusercontent.com/62598684/203058323-d2d1d8cd-b3f1-4dc4-9a20-d53975a7fcd4.jpeg)

# 2. Lane Detection 
Lane detection package allows Turtlebot3 to drive between two lanes without external influence. The robot was placed on the lane whereby the **yellow line** was on the left side of the robot, and the **white line** was placed on the right side of the robot. Here, the lane detection packages [Turtlebot3 E-Manual Robotics](https://emanual.robotis.com/docs/en/platform/turtlebot3/autonomous_driving/) were executed and the launch file basically runs the lane detection source code **detect_lane.py**. The nodes publishes the below topics after running the **rqt**:   
- **/detect/image_white_lane_marker/compressed**
- **/detect/image_yellow_lane_marker/compressed**
- **/detect/image_lane/compessed** which contains the reference line for the turtlebot3  trajectory.

Adjusts for the filter parameters can be changed by doing the **thresholding** of the **HSL** (hue, saturation and lightness) using the **rqt_reconfigure** to fine-tune the lines and the direction as such, the red line was overlaid on the yellow line while the blue line was overlaid on the white line.
![Detect_lane_rqt](https://user-images.githubusercontent.com/62598684/203061835-e03cc741-8a1d-44b8-962a-69cee6953456.jpeg)

Hue, Saturation and Lightness is a cylindrical color model that remaps the RGB primary colors into dimensions. Its idearly important to note that the three dimensions of the HSL color model are interdependent. If the value dimension of a color is set to 0%, the amount of hue and saturation does not matter as the color will be black. Likewise, if the saturation of a color is set to 0%, the hue does not matter as there is no color used. 

The following is what we get before making any modifications to our detection parameters : ![Lane detect 1](https://user-images.githubusercontent.com/62598684/203063436-b94a0d96-32cf-404e-b0f6-d5e434012d45.jpeg)

If you can observe the small screen on the fur right side of our image, the track is still showing its original color being black and not a full on green which gives us a good indication that we have made our lane detection successfully.

![Lane Detect 2](https://user-images.githubusercontent.com/62598684/203064861-10adc910-91e4-42b8-b286-d0e81275df44.jpeg)

Now we can conclude to say we have a good lane detection done as the little screen on the right has fully turned green which mean we can now go ahead and excute our trained robot to perform lane detection. To see our final outcome of what we learned to achieve lane detection, watch a video that we took of or turtlebot performing lane follow the link below : https://youtu.be/51OK6jKl1r0

## 3. (i) Tunnel Challenge 
We decided to make things intresting by adding a challenge for our turtlebot and see how it would perform after being placed in this situation. The tunnel challenge is the sixth mission of the obstacles that a turtlebot is given to overcome during autorace challenges. To make the tunnel challenge possible we change the navigation parameters in the turtlebot3/turtlebot3_navigation/param/ file. If you slam and make a new map, Place the new map to turtlebot3_autorace package you’ve placed /turtlebot3_autorace/turtlebot3_autorace_driving/maps/. We used the command lines that are given on the emanual robotis website under mission 8.5.6 tunnel mission and after running them we were able to get the following result: https://youtu.be/V8_kccn-lH8  /  https://youtu.be/4VAaIomIwQQ

## 3. (ii) Traffic Lights Challenge
Just to be extra, we decided to try the traffic challenge which is actually the first mission challenge on the autorace for a turtlebot3 and in most cases the traffic lights are placed at the beginning of the course before the turtlebot starts its challenge. Its definetly the same concept that auto race cars use before the start of there race, it predicts were they start, continue through or stop.

## Green_light Detection.
  ![Greenlight_detect](https://user-images.githubusercontent.com/62598684/203078163-e86f3538-85ef-435d-b25e-2ac435bc9fe0.jpeg)
  
  We werent able to get a full glipmse of the green light detection due to the fact that the bulbs on our traffic lights are quite small for our turtlebot to be able to obtain a full detection of the green traffic light. Among the 3 colors on our traffic lights, green was the only one that seemed to get a pro progressive answer than the others.
  
## Yellow_light Detection.
![Yellow_light detect](https://user-images.githubusercontent.com/62598684/203080970-85fdcdf2-1d7a-4534-93bf-3371a905b638.jpeg)
The yellow light proved to be quite redundant as the robot was able to detect it but also it saw the red coloring of the traffic stand to be part of its assigned detection.

## Red_Light Detection.
![Redlight_detect](https://user-images.githubusercontent.com/62598684/203085109-31283c13-1763-4e07-af7c-a508dece1278.jpeg)
The red light was a full waste on, as it detected the entire block as red, to sort out this problem i would sugguest that another traffic stand be printed probably not in a red color but maybe black and with bigger bulbs that will easily give out light for our turtlebot to be able to detect the colors easily.

## Traffic Sign Detection. 
TurtleBot3 can detect traffic signs using a node with SIFT algorithm, and perform programmed tasks while it drives on a built track. Follow the provided instructions to use Traffic sign detection. We used a sign with a white back ground as that seems to help the bot capture what its trying to detect.
With the implimentation of the SIFT algorithm, we were able to obtain the following results: 
## (i) https://www.youtube.com/watch?v=LplhjmSVGZI 
This implementation was illustrated on the screen record using the turtlebot3 camera, this was done without any signs placed in the view of the turtlebot camera.

## (ii) https://www.youtube.com/watch?v=Yhc69tsQK9Y
The above implementation was done with a sign placed in the view of the turtlebot3 which definetly gave a whhole different outcome.

## (iii) https://www.youtube.com/watch?v=3R1I3ja8NmE


  








