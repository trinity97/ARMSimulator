from ARMSimulator.src.python import setup


def run_arm_simulator():

    while setup.flag != 3:
        fetch()
        decode()
        execute()
        memory()
        write_back()


def fetch():
    setup.inst = setup.get_next_instruction(setup)
    print("FETCH instruction %s from address %s" %(setup.inst[4:],setup.inst[0:3]))


def decode():
    address = setup.inst[0:4]
    instruction = int(setup.inst[4:],0)
    setup.flag = (instruction>>26) & 0x3


def execute():
    setup.result = 0



def memory():
    print(2)


def write_back():
    print(5)
