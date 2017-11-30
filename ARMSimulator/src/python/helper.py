import sys
import setup


def read_file(name):
    file = open(name)
    setup.MEM = file.read().split("\n")
    setup.maximum = len(setup.MEM)


def get_next_instruction(setup):
    print("*******",setup.registers[15]//4)
    to_return = setup.MEM[setup.registers[15]//4]
    setup.registers[15] += 4

    return to_return


def exit():
    sys.exit()


def read():
    if setup.registers[0] == 0:
        setup.registers[0] = int(input())

def write():
    if setup.registers[0] == 1:
        print(setup.registers[1])



def print_execute(index):
    print("EXECUTE: %s %d and %d " % (setup.op_to_instruction.get(index),setup.registers[setup.firstOperand],setup.registers[setup.secondOperand]))
    write_to_out("EXECUTE: "+str(setup.op_to_instruction.get(index))+" "+str(setup.registers[setup.firstOperand]) + " and " + str(setup.registers[setup.secondOperand])+"\n")

def print_execute_imm(index):
    print("EXECUTE: %s %d and %d " % (setup.op_to_instruction.get(index),setup.registers[setup.firstOperand],setup.secondOperand))
    write_to_out("EXECUTE: "+str(setup.op_to_instruction.get(index))+" "+str(setup.registers[setup.firstOperand]) + " and " + str(setup.secondOperand)+"\n")


def print_execute_offset(index):
    print("EXECUTE: %s offset is: %d" % (setup.cond_to_instruction.get(index), setup.offset))
    write_to_out("EXECUTE: "+str(setup.op_to_instruction.get(index))+" offset is: "+str(setup.offset)+"\n")


def print_execute_ld(num):
    print("EXECUTE: Put in R%d, R%d's element number %d " % (setup.destination, setup.firstOperand, num+1))
    write_to_out("EXECUTE: Put in R" + str(setup.destination) + ",R"+ str(setup.firstOperand) +"'s element number "+ str(num+1)+"\n")


def print_execute_str(num):
    print("EXECUTE: Put R%d's value in element number %d in R%d " % (setup.firstOperand, num+1, setup.destination))
    write_to_out("EXECUTE: Put R"+str(setup.firstOperand)+"'s value in element number "+ str(num+1) + " in R"+ str(setup.destination)+"\n")



def int2bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    return s


def binToInt(binary_str):
    length = len(binary_str)
    num = 0

    for i in range(length):
        num = num + int(binary_str[i])
        num = num * 2
    return num / 2


def invert(num):
    num = int2bin(num)

    index = num.rfind('1')
    notChange = num[index:]
    change = num[0:index]
    emp = ""
    for i in change:
        if i=="1":
            emp+="0"
        else:
            emp+="1"
    ans = binToInt(emp+notChange)
    return int(ans)

def write_to_out(s):
    file = open("../../output/output.txt", "a")
    file.write(s)
    file.close()  # This close() is important


def reset_values():
    setup.MEM = [0] * 1000
    setup.registers = []
    setup.firstOperand = 0
    setup.secondOperand = 0
    setup.destination = 0
    setup.PC = 0
    setup.offset = 0
    setup.address = 0x0
    setup.flag = 0
    setup.op_code = 0
    setup.result = 0
    setup.cond = 0
    setup.immediate = 0
    setup.inst = ""
    setup.maximum = 0
    setup.Memory = {}
    setup.sig = 0
    setup.f1 = 0
    setup.f2 = 0

    for i in range(16):
        setup.registers.append(0)

    # setup.gui = 0










