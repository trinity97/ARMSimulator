import setup


def run_arm_simulator():

    while setup.flag != 3:
        fetch()
        decode()
        execute()
        memory()
        write_back()


def fetch():
    setup.inst = setup.get_next_instruction(setup)
    print("FETCH instruction %s from address %s" % (setup.inst[4:], setup.inst[0:3]))


def decode():
    address = setup.inst[0:4]
    instruction = int(setup.inst[4:], 0)
    setup.flag = (instruction >> 26) & 0x3
    setup.cond = (instruction >> 28) & 0xF

    if setup.flag==0 :
        setup.op_code = (instruction >> 21) & 0xF
        setup.immediate = (instruction >> 25) & 0x1
        setup.firstOperand = (instruction >> 16) & 0xF
        setup.destination = (instruction >> 12) & 0xF

        if setup.immediate ==0:
            setup.secondOperand = instruction & 0xF

            print("DECODE: Operation is %s, First Operand is R%d, Second Operand is R%d, Destination Register is R%d \nRead Registers: R%d = %d, R%d = %d\n" % (setup.op_to_instruction.get(setup.op_code),
                  setup.firstOperand, setup.secondOperand, setup.destination, setup.firstOperand,
                  setup.registers[setup.firstOperand], setup.secondOperand, setup.registers[setup.secondOperand]))

        elif setup.immediate == 1:
            setup.secondOperand = instruction & 0xFF

            print("DECODE: Operation is %s, First Operand is R%d, immediate Second Operand is %d, Destination Register is R%d \nRead Registers: R%d = %d\n" %
                  (setup.op_to_instruction.get(setup.op_code), setup.firstOperand, setup.secondOperand, setup.destination, setup.firstOperand,setup.registers[setup.firstOperand]))

    elif setup.flag == 1:
        setup.op_code = (instruction >> 20) & 0x3F
        setup.firstOperand = (instruction >> 16) & 0xF
        setup.secondOperand = instruction & 0xFFF
        setup.destination = (instruction >> 12) & 0xF

        print("DECODE: Operation is %s, Base Register is R%d, Offset is %d, Destination Register is R%d \n" %
              (setup.op_to_instruction.get(setup.op_code), setup.firstOperand, setup.secondOperand, setup.destination))

    elif setup.flag == 2:
        setup.op_code = (instruction >> 24) & 0x3
        setup.offset = instruction & 0xFFFFFF

        print("DECODE: Operation is %s" %
              setup.cond_to_instruction.get(setup.op_code))


def execute():
    setup.result = 0
    setup.to_be = 0



def memory():
    print(5)


def write_back():
    if setup.flag == 0:
        if setup.op_code != 10:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to %d" % (setup.result, setup.destination))
        else:
            print("WRITEBACK: no writeback required")
    elif setup.flag == 1:
        if setup.op_code == 25:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to %d" % (setup.result, setup.destination))
        elif setup.op_code == 24:
            setup.to_be = setup.registers[setup.destination]
            print("WRITEBACK: write %d to memory array" % setup.to_be)
    elif setup.flag == 2:
        print("WRITEBACK: No writeback operation required")



