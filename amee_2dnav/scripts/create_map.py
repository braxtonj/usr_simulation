#!/usr/bin/python
from __future__ import division
import numpy as np
import cv2

"""

Not a ROS node

Creates a pgm file for the map server
based on the arena

"""


H = 1000
W = 1000
border = 10
arena_width = 378
arena_height = 738

arena_map = np.zeros((H, W, 3), np.uint8)
# Clear out the inside of the arena
arena_map[border:border+arena_width, -arena_height-border:-border, :] = 255

# Clear the patches outside the arena
arena_map[:, :-(2*border+arena_height), :] = 255
arena_map[(2*border+arena_width):, :, :] = 255

cv2.imwrite('../maps/arena_map.pgm', arena_map)


print("y = -{}".format(((W - (2*border + arena_width) + border + arena_width/2) / 100 )))
print("x = -{}".format((H - (border + arena_height)) / 100 ))

