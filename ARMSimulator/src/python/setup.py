MEM = []

registers = {}
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

def read_file(name):
    file = open(name)
    MEM = file.read().split("\n")
    for i in MEM:
        print(i)
