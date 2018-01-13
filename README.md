# The Simulation packages

These packages contain the code specific to running the robot in simulation.


## Getting started

You should have Gazebo installed if you chose to install
ros-kinetic-desktop-full (recommended). You can test this with:
```
$ gazebo
```

If you do not have Gazebo, you will have to install it.  Google this. // TODO: give more instructions

NOTE: If you are using a virtual machine, Gazebo will run pretty slow and may not
work well at all.  

If Gazebo does work alright for you, then you can continue. First, install
all of the dependencies:

```
sudo apt-get -y install ros-kinetic-joy \
ros-kinetic-navigation \
ros-kinetic-robot-localization \
ros-kinetic-ros-control \
ros-kinetic-ros-controllers \
ros-kinetic-hector-gazebo-plugins # for imu sim \
ros-kinetic-move-base \
ros-kinetic-dwa-local-planner \
ros-kinetic-gazebo-ros-pkgs  \
ros-kinetic-gazebo-ros-control \
ros-kinetic-joint-state-controller \
ros-kinetic-effort-controllers \
ros-kinetic-position-controllers \
ros-kinetic-diff-drive-controller \
ros-kinetic-hector-gazebo-plugins
```

Also clone the aruco_pkgs repo:
```
git clone https://github.com/utahrobotics/aruco_pkgs.git
mv aruco_pkgs ~/catkin_ws/src
```

Then, clone the repo and try to build it. If you have any trouble,
please contact Matt. It should work, but if it doesn't, we want to
know why.

```
git clone https://github.com/utahrobotics/usr_simulation.git
mv usr_simulation ~/catkin_ws/src
cd ~/catkin_ws; catkin_make
```


If you are able to make everything, then try:
```
roslaunch amee_sim_control full_no_teleop.launch
```

You can also try driving it (if you have a controller) with:
NOTE: you will need to edit the launch config file to match whatever
controller you have.  It is currently set to PS3.
```
roslaunch amee_sim_control joy_teleop.launch
```


This should open up a simulation of the robot that you can control.
You can look at all the topics with:
```
rostopic list
```

Try publishing a message to the `/cmd/vel` topic:
```
rostopic pub -r 10 /cmd_vel geometry_msgs/Twist <TAB><TAB>
```

### amee_2dnav
This package holds configuration files for the ROS [navigation stack](http://wiki.ros.org/navigation).

You can set a move goal in RViz and the robot will go it.  To run this, you
will need to install the aruco_pkgs as described above.

```
roslaunch amee_2dnav amee_configuration.launch
```
and in a new terminal

```
roslaunch amee_2dnav move_base.launch
```

Then open up `rviz` and click with the 2D Nav Goal button to get the robot
to go to a certain place on the map.


### amee_sim_control
This package contains ros controllers that allow you to actually move the robot
in simulation.

To drive the robot base in simulation with a keyboard:
```
roslaunch amee_sim_control drive.launch
```

To use a controller, see the `joy_teleop.launch`. You may need to edit some
parameters.


Or, you can drive it via your own code/topics with `full_no_teleop.launch`.
You can publish to `/amee_arm_position_controller/command` (arm joint) or
`/amee_velocity_controller/cmd_vel` (driving).


```
roslaunch amee_sim_control full_no_teleop.launch

```

### amee_description

This packages hosts the urdf description of the robot and a launch file to
view it in rviz.

To view the robot in rviz:
`roslaunch amee_description display.launch`


### amee_gazebo
This package contains mostly xml, of launch files to display the robot in Gazebo
and descriptions of Gazebo worlds.

To just display the robot in simulation, without having control:
`roslaunch amee_gazebo gazebo.launch`  

#### Worlds
I have created a few custom worlds to place the robot in.  The nasa_minimal is
a simplified (boxy) version of the competition arena.  For a more realistic one,
use nasa_arena. Note: this requires more resources and if you contact the walls,
you fly far away.

You can also try messing around with custom worlds. See the gazebosim tutorials.


### TODOS
- Convert the code in the controller to listen to the main teleop node in amee.
- Convert other topics to be consistent with that used in the actual robot
#### For fun
##### Create a robot game in the simulation
Create a custom world, and use existing [Gazebo plugins][occupied_plugin] or
write your own to create a robot game in simulation.  It could be a teleop setup
or you could add autonomy components, so there is some challenge to program the
robot to solve a challenge.


[plugin_101]: http://gazebosim.org/tutorials?tut=plugins_hello_world&cat=write_plugin
[occupied_plugin]: http://gazebosim.org/tutorials?tut=occupiedevent&cat=plugins
