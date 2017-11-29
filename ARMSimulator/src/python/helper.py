import sys
import setup

def read_file(name,setup):
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


def print_execute(index):
    print("EXECUTE: %s %d and %d " % (setup.op_to_instruction.get(index),setup.registers[setup.firstOperand],setup.registers[setup.secondOperand]))

def print_execute_imm(index):
    print("EXECUTE: %s %d and %d " % (setup.op_to_instruction.get(index),setup.registers[setup.firstOperand],setup.secondOperand))

def print_execute_offset(index):
    print("EXECUTE: %s offset is: %d" % (setup.cond_to_instruction.get(index), setup.offset))

def print_execute_ld(num):
    print("EXECUTE: Put in R%d, R%d's element number %d " % (setup.destination, setup.firstOperand, num+1))

def print_execute_str(num):
    print("EXECUTE: Put R%d's value in element number %d in R%d " % (setup.firstOperand, num+1, setup.destination))


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