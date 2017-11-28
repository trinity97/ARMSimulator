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

def read_file(name,setup):
    file = open(name)
    setup.MEM = file.read().split("\n")
    setup.maximum = len(setup.MEM)


def get_next_instruction(setup):
    to_return = setup.MEM[setup.PC]
    setup.PC += 1
    return to_return



