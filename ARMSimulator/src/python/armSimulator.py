import setup
# import numpy
import helper

a=0
b=0
c=0
d=0


def run_arm_simulator():

    while setup.flag != 3:
        fetch()
        decode()
        execute()
        memory()
        write_back()


def fetch():
    setup.inst = helper.get_next_instruction(setup)
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

            print("DECODE: Operation is %s, First Operand is R%d, Second Operand is R%d, Destination Register is R%d \nRead Registers: R%d = %d, R%d = %d" % (setup.op_to_instruction.get(setup.op_code),
                  setup.firstOperand, setup.secondOperand, setup.destination, setup.firstOperand,
                  setup.registers[setup.firstOperand], setup.secondOperand, setup.registers[setup.secondOperand]))

        elif setup.immediate == 1:
            setup.secondOperand = instruction & 0xFF

            print("DECODE: Operation is %s, First Operand is R%d, immediate Second Operand is %d, Destination Register is R%d \nRead Registers: R%d = %d" %
                  (setup.op_to_instruction.get(setup.op_code), setup.firstOperand, setup.secondOperand, setup.destination, setup.firstOperand,setup.registers[setup.firstOperand]))

    elif setup.flag == 1:
        setup.op_code = (instruction >> 20) & 0x3F
        setup.firstOperand = (instruction >> 16) & 0xF
        setup.secondOperand = instruction & 0xFFF
        setup.destination = (instruction >> 12) & 0xF

        print("DECODE: Operation is %s, Base Register is R%d, Offset is %d, Destination Register is R%d " %
              (setup.op_to_instruction.get(helper.op_code), setup.firstOperand, setup.secondOperand, setup.destination))

    elif setup.flag == 2:
        setup.op_code = (instruction >> 24) & 0x3
        setup.offset = instruction & 0xFFFFFF

        #print ("-------", setup.cond)

        print("DECODE: Operation is %s" %
              setup.cond_to_instruction.get(setup.cond))


def execute():
    setup.result = 0

    if setup.flag == 0:

        if setup.immediate == 0:

            if setup.op_code == 0:

                helper.print_execute(0)
                setup.result = setup.registers[setup.firstOperand] & setup.registers[setup.secondOperand]

            elif setup.op_code == 1:

                helper.print_execute(1)
                setup.result = setup.registers[setup.firstOperand] ^ setup.registers[setup.secondOperand]

            elif setup.op_code == 2:
                helper.print_execute(2)
                setup.result = setup.registers[setup.firstOperand] - setup.registers[setup.secondOperand]

            elif setup.op_code == 4:
                helper.print_execute(4)
                setup.result = setup.registers[setup.firstOperand] + setup.registers[setup.secondOperand]

            elif setup.op_code == 5:
                helper.print_execute(5)
                setup.result = setup.registers[setup.firstOperand] + setup.registers[setup.secondOperand]

            elif setup.op_code == 10:
                helper.print_execute(10)

                if setup.registers[setup.firstOperand] == setup.registers[setup.secondOperand]:

                    setup.result = 0

                    setup.f1=1

                elif setup.registers[setup.firstOperand] < setup.registers[setup.secondOperand]:

                    setup.result = -1

                    setup.f2=1

                else:

                    setup.result = 1

            elif setup.op_code == 12:
                helper.print_execute(12)
                setup.result = setup.registers[setup.firstOperand] | setup.registers[setup.secondOperand]

            elif setup.op_code == 13:
                print ("EXECUTE: MOV value of R%d in R%d " % (setup.secondOperand, setup.destination))
                setup.result = setup.registers[setup.secondOperand]

            elif setup.op_code == 15:
                print ("EXECUTE: MNV NOT of R%d in R%d " % (setup.secondOperand, setup.destination))
                setup.result = ~setup.registers[setup.secondOperand]

        elif setup.immediate == 1:

            if setup.op_code == 0:

                helper.print_execute_imm(0)
                setup.result = setup.registers[setup.firstOperand] & setup.secondOperand

            elif setup.op_code == 1:

                helper.print_execute_imm(1)
                setup.result = setup.registers[setup.firstOperand] ^ setup.secondOperand

            elif setup.op_code == 2:

                helper.print_execute_imm(2)
                setup.result = setup.registers[setup.firstOperand] - setup.secondOperand

            elif setup.op_code == 4:

                helper.print_execute_imm(4)
                setup.result = setup.registers[setup.firstOperand] + setup.secondOperand

            elif setup.op_code == 5:

                helper.print_execute_imm(5)
                setup.result = setup.registers[setup.firstOperand] + setup.secondOperand

            elif setup.op_code == 10:

                helper.print_execute_imm(10)

                if setup.registers[setup.firstOperand] == setup.secondOperand:

                    setup.result = 0

                    setup.f1 = 1

                elif setup.registers[setup.firstOperand] < setup.secondOperand:

                    setup.result = -1

                    setup.f2 = 1

                else:

                    setup.result = 1

            elif setup.op_code == 12:

                helper.print_execute_imm(12)
                setup.result = setup.registers[setup.firstOperand] | setup.secondOperand

            elif setup.op_code == 13:

                print ("EXECUTE: MOV value of %d in R%d " % (setup.secondOperand, setup.destination))

                setup.result = setup.secondOperand

            elif setup.op_code == 15:

                print ("EXECUTE: MNV NOT of %d in R%d " % (setup.secondOperand, setup.destination))

                setup.result = ~setup.secondOperand

    elif setup.flag == 1:

        if setup.op_code == 25:

            k = setup.secondOperand / 4

            setup.print_execute_ld(k)

            setup.result = setup.temp.get(setup.firstOperand)[k]

        elif setup.op_code == 24:

            k = setup.secondOperand / 4

            setup.print_execute_str(k)

    elif setup.flag == 2:

        if setup.op_code == 2:

            bit = ((setup.offset >> 23) & 1)

            if bit == 1:

                setup.sig = (0xFF000000 | setup.offset)*4

                setup.sig = 0-(helper.invert(setup.sig))


            else:

                setup.sig = setup.offset*4

            helper.print_execute_offset(setup.cond)

            if setup.cond == 0:

                if setup.f1 == 1:

                    setup.registers[15] = setup.registers[15] + 4 + setup.sig

            elif setup.cond == 1:

                if setup.f1 != 1:

                    setup.registers[15] = setup.registers[15] + 4 + setup.sig

            elif setup.cond == 11:

                if setup.f2 == 1 and setup.f1 == 0:

                    setup.registers[15] = setup.registers[15] + 4 + setup.sig

            elif setup.cond == 12:

                if setup.f1 == 0 and setup.f2 == 0:

                    setup.registers[15] = setup.registers[15] + 4 + setup.sig

            elif setup.cond == 13:

                if setup.f1 == 1 or setup.f2 == 1:

                    setup.registers[15] = setup.registers[15] + 4 + setup.sig

            elif setup.cond == 14:

                setup.registers[15] = setup.registers[15] + 4 + setup.sig

            elif setup.cond == 10:

                if setup.f1 == 1 or setup.f2 == 0:

                    setup.registers[15] = setup.registers[15] + 4 + setup.sig



def memory():

    if setup.cond == 14:

        if setup.op_code == 24:

            k = setup.secondOperand/4

            print("MEMORY: Load %d from memory " % (setup.temp.get(setup.firstOperand)[k]))

        elif setup.op_code == 25:

            print("MEMORY: Store %d in memory " % setup.destination)

        else:

            print("MEMORY: No memory operation ")

    else :

        print ("MEMORY: No memory operation ")

def write_back():
    if setup.flag == 0:
        if setup.op_code != 10:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to R%d \n" % (setup.result, setup.destination))
        else:
            print("WRITEBACK: no writeback required \n")
    elif setup.flag == 1:
        if setup.op_code == 25:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to R%d \n" % (setup.result, setup.destination))
        elif setup.op_code == 24:
            k = setup.secondOperand//4
            setup.temp.get(setup.firstOperand)[k] = setup.registers[setup.destination]

            print("WRITEBACK: write %d to memory array" % setup.temp.get(setup.firstOperand)[k])
    elif setup.flag == 2:
        print("WRITEBACK: No writeback operation required \n")

    elif setup.flag == 3:
        print ("EXIT: \n")






