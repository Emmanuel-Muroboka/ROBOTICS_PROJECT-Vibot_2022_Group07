#!/bin/bash
#December 10, 2022.
#MISHECK EMMANUEL CHIRWA and BONIFACE SAMUEL IJEOMA
#Batch file to call our ROBOTICS_PROJECT launch files

#echo "Bringing up our turtlebot3 for movement...."


#Lane Detection
#step 1
#roscore&

#step2
#gnome-terminal -- sh -c "ssh ubuntu@192.168.0.200; bash"

#step3
roslaunch turtlebot3_autorace_camera raspberry_pi_camera_publish.launch; bash&

#step4
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch mode:=action; bash"

#step5
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_camera extrinsic_camera_calibration.launch mode:=action; bash"

#step6
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_detect detect_lane.launch mode:=action; bash"

gnome-terminal -- sh -c "rqt; bash"
#step7
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_driving turtlebot3_autorace_control_lane.launch; bash"

#step8
#gnome-terminal -- sh -c "roslaunch turtlebot3_bringup turtlebot3_robot.launch; bash"

#END


#Mission: Itersection
#roscore&
#gnome-terminal -- sh -c "ssh ubuntu@192.168.0.200; bash"

#step1 
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_camera intrinsic_camera_calibration.launch; bash"

#step2
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_core turtlebot3_autorace_core.launch mission:=intersection; bash"

#step3
gnome-terminal -- sh -c "roslaunch turtlebot3_autorace_core turtlebot3_autorace_mission.launch; bash"

#step4
gnome-terminal -- sh -c "rostopic pub -1 /core/decided_mode std_msgs/UInt8 "data: 2"; bash"

#step8
#gnome-terminal -- sh -c "roslaunch turtlebot3_bringup turtlebot3_robot.launch; bash"


#Mission: Stop sign detect
#code still in testing phase and not yet implented on turtlebot.
#Contains 10 images as for test
#To run
gnome-terminal -- sh -c " python3 detectStopSigns.py -p stopPrototype.png -i Stop\ Sign\ Dataset/1.png

