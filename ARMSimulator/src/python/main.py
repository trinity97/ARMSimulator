import setup
import armSimulator


if __name__ == '__main__':
    #setup.read_file("C:\\Users\\Abhishek Gupta\\PycharmProjects\\ARMSimulator\\ARMSimulator\\input\inputData.mem",setup)
    setup.read_file("../../input/fibonacci.mem", setup)

    for i in range(16):
        setup.registers.append(0)
    armSimulator.run_arm_simulator()

    #select_input_file.start_gui()