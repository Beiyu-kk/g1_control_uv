from g1_control.robot_arm.robot_arm import G1_29_ArmController
from g1_control.robot_arm.robot_arm import g1_move_right_arm_to_start


if __name__ == "__main__":
    g1_move_right_arm_to_start()

    arm = G1_29_ArmController(simulation_mode=True)
    # 获取当前arm速度和角度
    user_input = input("Please enter the start signal (enter 's' to start the next program): \n")
    if user_input.lower() == 's':
        q = arm.get_current_right_arm_q()
        dq = arm.get_current_right_arm_dq()
    print(q)
    print(dq)
    