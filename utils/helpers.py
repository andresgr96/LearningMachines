import numpy as np

def gripper(rob):
    in_gripper = 0
    front_irs = rob.read_irs()[5]

    # Use The frontal center sensor to detect if an objact is very close, then its gripped
    if front_irs <= 0.085:
        in_gripper = 1
        print("Grabbed")
    else:
        print("Not Grabbed")
        print(front_irs)

    return in_gripper
