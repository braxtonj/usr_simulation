cmake_minimum_required(VERSION 2.8.3)
project(amee_description)

find_package(catkin REQUIRED COMPONENTS
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES amee
 CATKIN_DEPENDS 
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

