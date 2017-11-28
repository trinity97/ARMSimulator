from ARMSimulator.src.python import setup


def run_arm_simulator():

    while True:
        fetch()
        decode()
        execute()
        memory()
        write_back()


def fetch():
    setup.inst = setup.get_next_instruction(setup)



def decode():
    print(1)


def execute():
    print(3)


def memory():
    print(2)


def write_back():
    print(5)
