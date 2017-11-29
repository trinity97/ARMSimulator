import sys

MEM = []
registers = []
firstOperand = 0
secondOperand = 0
destination = 0
PC = 0
offset = 0
address = 0x0
flag = 0
op_code = 0
result = 0
cond = 0
immediate = 0
inst = ""
maximum = 0
to_be = 0
Memory = {}
sig = 0
f1 = 0
f2 = 0

op_to_instruction = {0: "AND",
                     1: "XOR",
                     2: "SUB",
                     4: "ADD",
                     5: "ADC",
                     10: "CMP",
                     12: "ORR",
                     13: "MOV",
                     15: "MNV",
                     24: "STR",
                     25: "LDR"}

cond_to_instruction= {0: "BEQ",
                      1: "BNE",
                      10: "BGE",
                      11: "BLT",
                      12: "BGT",
                      13: "BLE",
                      14: "BAL"
                      }

temp = {0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
        13: [],
        14: [],
        15: []}

def read_file(name,setup):
    file = open(name)
    setup.MEM = file.read().split("\n")
    setup.maximum = len(setup.MEM)


def get_next_instruction(setup):
    to_return = setup.MEM[setup.PC]
    setup.PC += 1
    return to_return

def exit():

    sys.exit()





def print_execute(index):
    print("EXECUTE: %s %d and %d " % (op_to_instruction.get(index),registers[firstOperand],registers[secondOperand]))

def print_execute_imm(index):
    print("EXECUTE: %s %d and %d " % (op_to_instruction.get(index),registers[firstOperand],secondOperand))

def print_execute_offset(index):
    print("EXECUTE: %s offset is: %d" % (cond_to_instruction.get(index)), offset)

def print_execute_ld(num):
    print("EXECUTE: Put in R%d, R%d's element number %d " % (destination, firstOperand, num+1))

def print_execute_str(num):
    print("EXECUTE: Put R%d's value in element number %d in R%d " % (firstOperand, num+1, destination))
