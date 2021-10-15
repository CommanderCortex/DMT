#!/usr/bin/env python3

import sys
import subprocess

# Custom Enum for Operations
dmt_counter=0
def dmtCounter(reset=False):
    global dmt_counter
    if reset:
        dmt_counter = 0
    result = dmt_counter
    dmt_counter += 1
    return result

#Operations
OP_PUSH=dmtCounter(True)
OP_PLUS=dmtCounter()
OP_MINUS=dmtCounter()
OP_DISPLAY=dmtCounter()
OP_RAWSTACK=dmtCounter()
OP_DUMP=dmtCounter()
COUNT_OPS=dmtCounter()

#Operations Definded as usable code:
def mov(x):
    return (OP_PUSH, x)

def add():
    return (OP_PLUS, )

def sub():
    return (OP_MINUS, )

def hlt():
    return (OP_DUMP, )

def stk():
    return(OP_RAWSTACK, )

def dis():
    return (OP_DISPLAY, )    

#Simulate Code with an interpretor:
def simulateProgram(program):
    stack = []
    for op in program:
        assert COUNT_OPS == 6, "Expected Operation Handling Error"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif op[0] == OP_DISPLAY:
            z = stack.pop()
            print(z)
        elif op[0] == OP_RAWSTACK:
            print("Current Stack:", stack)        
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        else:
            assert False, "Unreachable"    

#Compile code in Assembly for Execution
def compileProgram(program, out_file_path):
    with open(out_file_path, "w") as out:
        out.write("segment .text\n")
        #Dump Func 
        out.write("global _start\n")
        out.write("_start:\n")
        for op in program:
            assert COUNT_OPS == 6, "Expected Operation Handling Error"
            if op[0] == OP_PUSH:
                out.write("     ;; -- mov %d --\n" % op[1])
                out.write("     push %d\n" % op[1])
            elif op[0] == OP_PLUS:
                out.write("     ;; -- add --\n")
                out.write("     pop rax\n")
                out.write("     pop rbx\n")
                out.write("     add rax, rbx\n")
                out.write("     push rax\n")
            elif op[0] == OP_MINUS:
                out.write("     ;; -- sub --\n")
                out.write("     pop rax\n")
                out.write("     pop rbx\n")
                out.write("     sub rbx, rax\n")
                out.write("     push rax\n")
            elif op[0] == OP_RAWSTACK:
                out.write("     ;; -- stk --\n")
                out.write("     ;; -- TODO")
            elif op[0] == OP_DISPLAY:
                out.write("     ;; -- dis --\n")
                out.write("     ;; -- TODO")
            elif op[0] == OP_DUMP:
                out.write("     ;; -- hlt --\n")
                out.write("     pop rbx\n")
                #out.write("     call dump\n")
            else:
                assert False, "Unreachable"
        out.write("     mov rax, 60\n")
        out.write("     mov rdi, 0\n")
        out.write("     syscall\n")

#Code for Compilation & Simulation
# TODO: unhardcode program
program=[
    stk(),
    mov(34), 
    mov(35),
    stk(),
    add(),
    hlt(),
    ]        

def usage():
    print("Usage: DMT <SUBCOMMAND> [ARGS]")
    print("SUBCOMMANDS:")
    print("    sim        Simulate the program")
    print("    com        Compile the Program")

def call_cmd(cmd):
    print(cmd)
    subprocess.call(cmd)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        print("Please provide a subcommand")
        exit(1)

    subcommand = sys.argv[1]

    if subcommand == "sim":
        simulateProgram(program)
    elif subcommand == "com":
        compileProgram(program, "test.asm")
        call_cmd(["nasm", "-felf64", "test.asm"])
        call_cmd(["ld", "-o", "test", "test.o"])
        #call_cmd(["rm", "output.asm", "output.o"])

    else:
        usage()
        print("ERROR: Unknow subcommand %s" % (subcommand))
        exit(1)
