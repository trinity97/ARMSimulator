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


def write_back():
    if setup.flag == 0:
        if setup.op_code != 10:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to %d" %(setup.result,setup.destination))
        else:
            print("WRITEBACK: no writeback required")
    elif setup.flag == 1:
        if setup.op_code == 25:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to %d" %(setup.result, setup.destination))
        elif setup.op_code == 24:
            setup.to_be = setup.registers[setup.destination]
            print("WRITEBACK: write %d to memory array" % setup.to_be)
    elif setup.flag == 2:
        print("WRITEBACK: No writeback operation required")


def memory():
    print(5)
