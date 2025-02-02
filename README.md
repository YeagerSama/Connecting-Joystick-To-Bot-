# Connecting-Joystick-To-Bot:

This tutorial will guide you to connect your joystick to your dev machine which will be inturn connected to your bot(robot).This way you would experience a slight more latency than directly connecting the joystick to the bot but this way is more beginner friendly, and will be used in the following tutorial.Regardless, you can follow along by changing a few commands and performing the coding part on the microcontroller connected to your bot. 

In this tutorial I will be using a Microsoft Xbox Controller with a dongle, and will be controlling the turtle bot (Turtlesim).Follow along!

# Pre-Requisites:

1.Joystick/Gamepad
2.Basic knowledge of ROS2 Publisher-Subscriber concepts
3.Crearting a launch file(optional)

# Installation Steps:

joystick – Provides the jstest and jscal utilities for testing and calibrating joystick devices.
jtest-gtk – A GTK-based graphical joystick testing tool.
evtest – A command-line utility for monitoring input device events, useful for debugging joystick inputs.

```
sudo apt upgrade
sudo apt install joystick jstest-gtk evtest
```
The command adds tools to test and check joysticks on your Linux computer.

# Checking and controlling the JoyStick:

Run the command:
```
evtest
```
-Usually, the last number from the range given is the ID of the 
 controller.
-Move the joystick/gamepad to confirm that it's detected and working.
-If sucessful, you will see values updating in the terminal, indicating that Linux recognizes the device.

# Visualize Joystick Input with jstest-gtk:

Run the command:
```
jstest-gtk


