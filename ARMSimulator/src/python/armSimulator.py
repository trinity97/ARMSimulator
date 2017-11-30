import setup
# import numpy
import helper
import select_input_file

a=0
b=0
c=0
d=0


def run_arm_simulator():

    while True:
        fetch()
        decode()
        execute()
        memory()
        write_back()
        helper.write_to_out("\n")
        # setup.gui.editor()


def step_into():

    fetch()
    decode()
    execute()
    memory()
    write_back()
    helper.write_to_out("\n")

def fetch():
    setup.inst = helper.get_next_instruction(setup)
    print(setup.inst)
    print("FETCH instruction %s from address %s" % (setup.inst[4:], setup.inst[0:3]))
    helper.write_to_out("FETCH instruction "+ str(setup.inst[4:])+" from address "+str(setup.inst[0:3]+"\n"))
    setup.gui.editor("FETCH instruction "+ str(setup.inst[4:])+" from address "+str(setup.inst[0:3]+"\n"))


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
            helper.write_to_out("DECODE: Operation is "+ str(setup.op_to_instruction.get(setup.op_code))+ ", First Operand is R"+ str(setup.firstOperand) + ", Second Operand is R"+ str(setup.secondOperand)+ ", Destination Register is R"+ str(setup.destination)+ " \nRead Registers: R"+ str(setup.firstOperand)+ " = "+ str(setup.registers[setup.firstOperand]) + ", R"+ str(setup.secondOperand) + " = " + str(setup.registers[setup.secondOperand])+"\n")
            setup.gui.editor("DECODE: Operation is "+ str(setup.op_to_instruction.get(setup.op_code))+ ", First Operand is R"+ str(setup.firstOperand) + ", Second Operand is R"+ str(setup.secondOperand)+ ", Destination Register is R"+ str(setup.destination)+ " \nRead Registers: R"+ str(setup.firstOperand)+ " = "+ str(setup.registers[setup.firstOperand]) + ", R"+ str(setup.secondOperand) + " = " + str(setup.registers[setup.secondOperand])+"\n")

        elif setup.immediate == 1:
            setup.secondOperand = instruction & 0xFF

            print("DECODE: Operation is %s, First Operand is R%d, immediate Second Operand is %d, Destination Register is R%d \nRead Registers: R%d = %d" %
                  (setup.op_to_instruction.get(setup.op_code), setup.firstOperand, setup.secondOperand, setup.destination, setup.firstOperand,setup.registers[setup.firstOperand]))

            helper.write_to_out("DECODE: Operation is "+ str(setup.op_to_instruction.get(setup.op_code))+ ", First Operand is R"+ str(setup.firstOperand) + ", immediate Second Operand is "+ str(setup.secondOperand)+ ", Destination Register is R"+ str(setup.destination)+ " \nRead Registers: R"+ str(setup.firstOperand)+ " = "+ str(setup.registers[setup.firstOperand]) + "\n")
            setup.gui.editor("DECODE: Operation is "+ str(setup.op_to_instruction.get(setup.op_code))+ ", First Operand is R"+ str(setup.firstOperand) + ", immediate Second Operand is "+ str(setup.secondOperand)+ ", Destination Register is R"+ str(setup.destination)+ " \nRead Registers: R"+ str(setup.firstOperand)+ " = "+ str(setup.registers[setup.firstOperand]) + "\n")

    elif setup.flag == 1:
        setup.op_code = (instruction >> 20) & 0x3F
        setup.firstOperand = (instruction >> 16) & 0xF
        setup.secondOperand = instruction & 0xFFF
        setup.destination = (instruction >> 12) & 0xF

        print("DECODE: Operation is %s, Base Register is R%d, Offset is %d, Destination Register is R%d " %
              (setup.op_to_instruction.get(setup.op_code), setup.firstOperand, setup.secondOperand, setup.destination))

        helper.write_to_out("DECODE: Operation is "+str(setup.op_to_instruction.get(setup.op_code))+", Base Register is R" + str(setup.firstOperand) +", Offset is "+str(setup.secondOperand)+", Destination Register is R"+str(setup.destination)+"\n")
        setup.gui.editor("DECODE: Operation is "+str(setup.op_to_instruction.get(setup.op_code))+", Base Register is R" + str(setup.firstOperand) +", Offset is "+str(setup.secondOperand)+", Destination Register is R"+str(setup.destination)+"\n")

    elif setup.flag == 2:
        setup.op_code = (instruction >> 24) & 0x3
        setup.offset = instruction & 0xFFFFFF

        #print ("-------", setup.cond)

        print("DECODE: Operation is %s" %
              setup.cond_to_instruction.get(setup.cond))
        helper.write_to_out("DECODE: Operation is "+str(setup.cond_to_instruction.get(setup.cond))+"\n")
        setup.gui.editor("DECODE: Operation is "+str(setup.cond_to_instruction.get(setup.cond))+"\n")

    elif setup.flag == 3:

        mask = instruction & 0xFF
        print("DECODE: Operation is %s " % (setup.swi.get(mask)) + "\n")
        helper.write_to_out("DECODE: Operation is %s " % (setup.swi.get(mask)) + "\n")
        setup.gui.editor("DECODE: Operation is %s " % (setup.swi.get(mask)) + "\n")




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
                helper.write_to_out("EXECUTE: MOV value of R" + str(setup.secondOperand) + " in R" + str(setup.destination) + "\n")
                setup.gui.editor("EXECUTE: MOV value of R" + str(setup.secondOperand) + " in R" + str(setup.destination) + "\n")
                setup.result = setup.registers[setup.secondOperand]

            elif setup.op_code == 15:
                print ("EXECUTE: MNV NOT of R%d in R%d " % (setup.secondOperand, setup.destination))
                setup.result = ~setup.registers[setup.secondOperand]
                helper.write_to_out("EXECUTE: MNV NOT of R" + str(setup.secondOperand) + " in R" + str(setup.destination) + "\n")
                setup.gui.editor("EXECUTE: MNV NOT of R" + str(setup.secondOperand) + " in R" + str(setup.destination) + "\n")

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
                helper.write_to_out("EXECUTE: MOV value of " + str(setup.secondOperand) + " in R" + str(setup.destination) + "\n")
                setup.gui.editor("EXECUTE: MOV value of " + str(setup.secondOperand) + " in R" + str(setup.destination) + "\n")

                setup.result = setup.secondOperand

            elif setup.op_code == 15:

                print ("EXECUTE: MNV NOT of %d in R%d " % (setup.secondOperand, setup.destination))
                setup.gui.editor("EXECUTE: MNV NOT of "+ str(setup.secondOperand) +" in R"+ str(setup.destination) +"\n")

                setup.result = ~setup.secondOperand

    elif setup.flag == 1:

        if setup.op_code == 25:

            k = setup.secondOperand // 4

            helper.print_execute_ld(k)

            setup.result = setup.temp.get(setup.firstOperand)[k]

        elif setup.op_code == 24:

            k = setup.secondOperand // 4

            helper.print_execute_str(k)

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

    elif setup.flag == 3:

        print("EXECUTE: No Execution \n")
        helper.write_to_out("EXECUTE: No Execution \n")
        setup.gui.editor("EXECUTE: No Execution \n")


def memory():

    if setup.cond == 14:

        if setup.op_code == 24:

            k = setup.secondOperand//4

            print("MEMORY: Load %d from memory " % (setup.temp.get(setup.firstOperand)[k]))
            helper.write_to_out("MEMORY: Load "+str(setup.temp.get(setup.firstOperand)[k])+" from memory \n")
            setup.gui.editor("MEMORY: Load "+str(setup.temp.get(setup.firstOperand)[k])+" from memory \n")

        elif setup.op_code == 25:

            print("MEMORY: Store %d in memory " % setup.destination)
            helper.write_to_out("MEMORY: Store "+str(setup.destination)+" in memory \n")
            setup.gui.editor("MEMORY: Store "+str(setup.destination)+" in memory \n")

        else:

            print("MEMORY: No memory operation ")
            helper.write_to_out("MEMORY: No memory operation \n")
            setup.gui.editor("MEMORY: No memory operation \n")

    else:
        print("MEMORY: No memory operation ")
        helper.write_to_out("MEMORY: No memory operation \n")
        setup.gui.editor("MEMORY: No memory operation \n")


def write_back():
    if setup.flag == 0:
        if setup.op_code != 10:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to R%d \n" % (setup.result, setup.destination))
            helper.write_to_out("WRITEBACK: write "+str(setup.result)+" to R"+str(setup.destination)+" \n")
            setup.gui.editor("WRITEBACK: write "+str(setup.result)+" to R"+str(setup.destination)+" \n")
        else:
            print("WRITEBACK: no writeback required \n")
            helper.write_to_out("WRITEBACK: no writeback required \n")
            setup.gui.editor("WRITEBACK: no writeback required \n")
    elif setup.flag == 1:
        if setup.op_code == 25:
            setup.registers[setup.destination] = setup.result
            print("WRITEBACK: write %d to R%d \n" % (setup.result, setup.destination))
            helper.write_to_out("WRITEBACK: write "+str(setup.result)+" to R"+str(setup.destination)+" \n")
            setup.gui.editor("WRITEBACK: write "+str(setup.result)+" to R"+str(setup.destination)+" \n")
        elif setup.op_code == 24:
            k = setup.secondOperand//4
            setup.temp.get(setup.firstOperand)[k] = setup.registers[setup.destination]

            print("WRITEBACK: write %d to memory array" % setup.temp.get(setup.firstOperand)[k])
            helper.write_to_out("WRITEBACK: write "+str(setup.temp.get(setup.firstOperand)[k])+" to memory array \n")
            setup.gui.editor("WRITEBACK: write "+str(setup.temp.get(setup.firstOperand)[k])+" to memory array \n")
    elif setup.flag == 2:
        print("WRITEBACK: No writeback operation required \n")
        helper.write_to_out("WRITEBACK: No writeback operation required \n")
        setup.gui.editor("WRITEBACK: No writeback operation required \n")
    elif setup.flag == 3:
        mask = int(setup.inst[4:0], 0) & 0xFF
        if mask == 0x11:
            print("EXIT: \n")
            helper.write_to_out("EXIT: \n")
            setup.gui.editor("EXIT: \n")
        elif mask == 0x6C:
            helper.read()
            print("WRITEBACK: %s is Read from Console and stored in Register 0" % str(setup.register[0]))
            helper.write_to_out("WRITEBACK: %s is Read from File and stored in Register 0" % str(setup.register[0]))
            setup.gui.editor("WRITEBACK: %s is Read from File and stored in Register 0" % str(setup.register[0]))
        elif mask == 0x6B:
            helper.write()
            print("WRITEBACK: %s is Written to Console from Register 1" % str(setup.register[1]))
            helper.write_to_out("WRITEBACK: %s is Written to Console from Register 1" % str(setup.register[1]))
            setup.gui.editor("WRITEBACK: %s is Written to Console from Register 1" % str(setup.register[1]))

    setup.gui.registers()