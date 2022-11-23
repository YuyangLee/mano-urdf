'''
Author: Aiden Li
Date: 2022-11-23 17:54:19
LastEditors: Aiden Li (i@aidenli.net)
LastEditTime: 2022-11-23 18:00:48
Description: Your description
'''
import numpy as np
from urdfpy import URDF

robot = URDF.load("urdf/mano.urdf")

robot.animate(cfg_trajectory={
    # "j_index1y":    [0.0, np.pi / 4],
    "j_index1x":    [0.0, np.pi / 4],
    "j_index2":     [0.0, np.pi / 4],
    "j_index3":     [0.0, np.pi / 4],
    # "j_middle1y":   [0.0, np.pi / 4],
    "j_middle1x":   [0.0, np.pi / 4],
    "j_middle2":    [0.0, np.pi / 4],
    "j_middle3":    [0.0, np.pi / 4],
    # "j_pinky1y":    [0.0, np.pi / 4],
    "j_pinky1x":    [0.0, np.pi / 4],
    "j_pinky2":     [0.0, np.pi / 4],
    "j_pinky3":     [0.0, np.pi / 4],
    # "j_ring1y":     [0.0, np.pi / 4],
    "j_ring1x":     [0.0, np.pi / 4],
    "j_ring2":      [0.0, np.pi / 4],
    "j_ring3":      [0.0, np.pi / 4],
    "j_thumb1y":    [0.0, np.pi / 4],
    # "j_thumb1z":    [0.0, np.pi / 4],
    "j_thumb2":     [0.0, np.pi / 4],
    "j_thumb3":     [0.0, np.pi / 4]
})