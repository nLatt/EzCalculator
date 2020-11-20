
main = """
import re

def calculator(): 
    print(\"I will multiply both of your inputs\")
    
    operation = input("please enter your operation (max {max_operands} operands and no number should be over {max_number}): ")

    operation = re.sub("[\s]+", " ", operation.strip()).split(" ")

    operands = ["+", "-", "/", "*"]

    if len(operation) >= 3:
        for i in range(0, len(operation)):
            if i != 0:
                current = operation[i]
                preceeding = operation[i - 1]

                if not ((current.isdigit() and preceeding in operands) or (current in operands and preceeding.isdigit())):
                    print("This was not a valid operation")
                    return
    else:
        print("This was not a valid operation")\n
"""

indentation = "    "


def generator(max_number, max_operands):
    calculator = open("calculator.py", "w")
    signs = ["+", "-", "/", "*"]

    prepare_main = main.format(max_operands = max_operands, max_number = max_number)
    calculator.write(prepare_main)
    x = [0 for i in range(max_operands)]
    print(x)
    for sign in signs:
        calc_creator(max_number, max_operands, sign, calculator)
        print("---------\n")

    return

"""
    for sign in signs:
        for first in range(1, max_number + 1):
            for second in range(1, max_number + 1):
                #prepare_if_statement = indentation + "if "
                prepare_if_statement = "first == {} and sign == \"{}\" and second == {}:\n".format(first, sign, second)



                prepare_calculation = indentation + "result = {} {} {}\n".format(first, sign, second)
                prepare_print_result = indentation + "print(\"{} {} {} =\", result)\n\n".format(first, sign, second)
                prepare_if = prepare_if_statement + prepare_calculation + prepare_print_result

                calculator.write(prepare_if)
    calculator.write("calculator()\n\n")
"""

def calc_creator(max_number, operand_nbr, sign, calculator, test = "    if "):
    for x in range(1, max_number + 1):
        print(x)
        test += "operation[{}] == {}\n".format(operand_nbr, max_number)
        calculator.write(test)

        if operand_nbr > 0:
            operand_nbr -= 1
            print(operand_nbr, "operand")
            calc_creator(max_number, operand_nbr, sign, calculator)  
        



generator(10, 3)
