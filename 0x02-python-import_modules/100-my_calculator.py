#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys

    ops = ["+", "-", "*", "/"]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        
        if sys.argv[2] == "+":
            print(f"{a} {sys.argv[2]} {b} = {add(a, b)}")
    
        if sys.argv[2] == "-":
            print(f"{a} {sys.argv[2]} {b} = {sub(a, b)}")
        
        if sys.argv[2] == "*":
            print(f"{a} {sys.argv[2]} {b} = {mul(a, b)}")
        
        if sys.argv[2] == "/":
            print(f"{a} {sys.argv[2]} {b} = {div(a, b)}")
