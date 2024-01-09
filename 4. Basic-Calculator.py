# Basic Calculator
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    num1 = float(input("enter 1st number: "))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("enter 2nd number: "))
        user = operations[operation_symbol]
        answer = user(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("do you want to continue to calculate with answer type yes or no: ") == "yes":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()



# Output:
enter 1st number: 456.9876
+
-
*
/
pick an operation: +
enter 2nd number: 56.98
456.9876 + 56.98 = 513.9676
do you want to continue to calculate with answer type yes or no: yes
pick an operation: +
enter 2nd number: 20
513.9676 + 20.0 = 533.9676
do you want to continue to calculate with answer type yes or no: yes
pick an operation: -
enter 2nd number: 500
533.9676 - 500.0 = 33.96759999999995
do you want to continue to calculate with answer type yes or no: yes
pick an operation: /
enter 2nd number: 3
33.96759999999995 / 3.0 = 11.322533333333316
do you want to continue to calculate with answer type yes or no: no
enter 1st number: 12
+
-
*
/
pick an operation: +
enter 2nd number: 15
12.0 + 15.0 = 27.0
do you want to continue to calculate with answer type yes or no: no
enter 1st number: 
