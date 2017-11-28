from ARMSimulator.src.python import setup
from ARMSimulator.src.python import armSimulator

if __name__ == '__main__':
    setup.read_file("C:\\Users\\Abhishek Gupta\\PycharmProjects\\ARMSimulator\\ARMSimulator\\input\inputData.mem",setup)
    armSimulator.run_arm_simulator()