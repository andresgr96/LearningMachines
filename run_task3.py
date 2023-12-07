#!/usr/bin/env python3

from __future__ import print_function
import numpy as np
import cv2
import sys
import signal
from src import robobo
from src.LearningMachines.controllers.controller import Controller
from src.LearningMachines.utils.infra_sensors import gripper


def terminate_program(signal_number, frame):
    print("Ctrl-C received, terminating program")
    sys.exit(1)


def main():
    # Start sim setup
    signal.signal(signal.SIGINT, terminate_program)
    rob = robobo.SimulationRobobo().connect(address='127.0.0.1', port=19997)
    rob.play_simulation()
    rob.set_phone_tilt(0.9, 100)
    # rob.randomize_position()

    # Simulation run variables
    controller = Controller  # Test controller, just outputs random numbers
    max_steps = 50
    steps = 0

    # Fitness/Reward Variables
    fitness = 0
    steps_food_in_gripper = 0
    initial_food_distance = 0

    for i in range(max_steps):
        left, right = controller.control(rob)
        rob.move(left, right, 200)

        #
        if gripper(rob):
            steps_food_in_gripper += 1
        steps += 1

    gripper_reward = 20 * (steps_food_in_gripper / steps)
    fitness += gripper_reward
    print(f"Final fitness: {fitness}")
    rob.stop_world()
    rob.wait_for_stop()


if __name__ == "__main__":
    main()
