import sys

MEM = [0] * 1000
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

temp = {0: [0] * 1024,
        1: [0] * 1024,
        2: [0] * 1024,
        3: [0] * 1024,
        4: [0] * 1024,
        5: [0] * 1024,
        6: [0] * 1024,
        7: [0] * 1024,
        8: [0] * 1024,
        9: [0] * 1024,
        10: [0] * 1024,
        11: [0] * 1024,
        12: [0] * 1024,
        13: [0] * 1024,
        14: [0] * 1024,
        15: [0] * 1024}

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
    print("EXECUTE: %s %d and %d " % (op_to_instruction.get(index),registers[firstOperand],registers[secondOperand]))

def print_execute_imm(index):
    print("EXECUTE: %s %d and %d " % (op_to_instruction.get(index),registers[firstOperand],secondOperand))

def print_execute_offset(index):
    print("EXECUTE: %s offset is: %d" % (cond_to_instruction.get(index), offset))

def print_execute_ld(num):
    print("EXECUTE: Put in R%d, R%d's element number %d " % (destination, firstOperand, num+1))

def print_execute_str(num):
    print("EXECUTE: Put R%d's value in element number %d in R%d " % (firstOperand, num+1, destination))


def int2bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
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