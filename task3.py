#!/usr/bin/env python3
from __future__ import print_function

import time
import numpy as np
import cv2
import sys
import signal
from src import robobo
from src.LearningMachines.utils.computer_vision import red_mask, segment_image, detect_objects


def terminate_program(signal_number, frame):
    print("Ctrl-C received, terminating program")
    sys.exit(1)


def main():
    signal.signal(signal.SIGINT, terminate_program)
    # rob = robobo.HardwareRobobo(camera=True).connect(address="192.168.1.7")

    rob = robobo.SimulationRobobo().connect(address='127.0.0.1', port=19997)
    mask_window = 'mask'
    segment_window = 'segments'

    moving = True
    turning = False

    rob.play_simulation()
    rob.set_phone_tilt(0.9,100)

    while True:
        # Show masked image
        image = rob.get_image_front()
        mask = red_mask(image)
        segmented = segment_image(image)
        detect_objects(mask)
        cv2.imshow(segment_window, segmented)
        # cv2.imshow(mask_window, mask)
        cv2.waitKey(1)

        try:
            center_sen = np.log(rob.read_irs()[5]) / 10
            back_sen = np.log(rob.read_irs()[1]) / 10
            # print("Center Sensor: " + str(center_sen))
            # print("Back Sensor: " + str(back_sen))
        except:
            print(f"Error reading proximity sensors")
            time.sleep(0.1)
            continue

        if moving:
            # print("robobo is at {}".format(rob.position()))

            # rob.move(8, 8, 200)
            print("State: Moving")



            # # Save img if needed
            # cv2.imwrite("imgs/test_img.png", image)


            # if -100 < center_sen <= -0.17:
            #     # Following code gets an image from the camera
            #     # image = rob.get_image_front()
            #     # # IMPORTANT! `image` returned by the simulator is BGR, not RGB
            #     # cv2.imwrite("imgs/test_img.png", image)
            #     break





    time.sleep(0.1)

    # # IR reading
    # for i in range(10000):
    #     print("ROB Irs: {}".format(np.log(np.array(rob.read_irs())) / 10))
    #     time.sleep(0.1)

    # pause the simulation and read the collected food
    rob.pause_simulation()

    # Stopping the simualtion resets the environment
    rob.stop_world()


if __name__ == "__main__":
    main()
