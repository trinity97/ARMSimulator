import setup
import armSimulator
import helper
import select_input_file

if __name__ == '__main__':
    #setup.read_file("C:\\Users\\Abhishek Gupta\\PycharmProjects\\ARMSimulator\\ARMSimulator\\input\inputData.mem",setup)
    # helper.read_file("../../input/inputData.mem", setup)



    file = open("../../output/output.txt", "w")
    file.write("")


    # armSimulator.run_arm_simulator()


    select_input_file.start_gui()