from robot_arm import *
from ipc_example import *


if __name__ == "__main__":
    g1_move_right_arm_to_start()

    arm = G1_29_ArmController(simulation_mode=True)
    # 获取当前arm速度和角度
    user_input = input("Please enter the start signal (enter 's' to start the next program): \n")
    if user_input.lower() == 's':
        q = arm.get_current_right_arm_q()
        dq = arm.get_current_right_arm_dq()
    