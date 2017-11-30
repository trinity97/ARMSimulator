import sys
import helper

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

gui = 0

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

swi = { 0x6b: " Write integer to File ", 0x6c: 'Read integer from file', 0x11: "Exit"}
