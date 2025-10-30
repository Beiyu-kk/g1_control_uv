import logging_mp
logging_mp.basic_config(level=logging_mp.INFO)
logger_mp = logging_mp.get_logger(__name__)

from g1_control.robot_arm import robot_arm


robot_arm.g1_move_right_arm_to_start()