import numpy as np

def gripper(rob):
    in_gripper = 0
    front_irs = rob.read_irs()[5]

    # Use The frontal center sensor to detect if an object is very close, then its gripped
    if front_irs <= 0.085:
        in_gripper = 1
        print("Grabbed")
    # else:
    #     print("Not Grabbed")
    #     print(front_irs)

    return [in_gripper]


def get_irs_sensors(rob):
    irs_sensors = rob.read_irs()
    b_right = irs_sensors[0]
    b_cent = irs_sensors[1]
    b_left = irs_sensors[2]
    f_right2 = irs_sensors[3]
    f_right = irs_sensors[4]
    f_cent = irs_sensors[5]
    f_left = irs_sensors[6]
    f_left2 = irs_sensors[7]

    return [b_right, b_cent, b_left, f_right2, f_right, f_cent, f_left, f_left2]
