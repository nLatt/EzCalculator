main = """
print(\"I will multiply both of your inputs\")

first = int(input("First number: "))
sign = input("Operator +-/*: ")
second = int(input("Second number: "))

"""

indentation = "    "


def generator(max_number):
    calculator = open("calculator_simple.py", "w")
    signs = ["+", "-", "/", "*"]

    calculator.write(main)
    for sign in signs:
        for first in range(1, max_number + 1):
            for second in range(1, max_number + 1):
                prepare_if_statement = "if first == {} and sign == \"{}\" and second == {}:\n".format(first, sign, second)
                prepare_calculation = indentation + "result = {} {} {}\n".format(first, sign, second)
                prepare_print_result = indentation + "print(\"{} {} {} =\", result)\n\n".format(first, sign, second)

                prepare_if = prepare_if_statement + prepare_calculation + prepare_print_result
                calculator.write(prepare_if)


    return

generator(10)
