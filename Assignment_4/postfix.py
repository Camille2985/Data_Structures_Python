# postfix.py
# Author: Camille Church
# Date 12/20/2021
# Inputs: A file of equations in Postfix notation in lines format
# Outputs: A file of solutions to the equation
# Expected Behavior: Program will process file of equations and output the solutions to a
#   to a single file


class PostfixEquation:
    def __init__(self, equation):
        self.equation = equation
        self.solution = self.main()

    # Solves the postfix equation by iterating by:
    # 1. Breaking the equation into an array
    # 2. Iterating through the array to find the operation elements
    # 3. When it finds one:
    #       a. Performs the operation on the previous 2 items in the array
    #       b. Deletes three elements (2 operands and 1 operator)
    #       c. Places the new value into the position of the first operand
    #       d. Resets the iterator to 0
    #       e. Continues loop
    # 4. When loop is finished and there are no more operations to be preformed
    #    the final value is returned
    def main(self):
        array_of_operands = self.equation.split()
        length = len(array_of_operands)
        i = 0

        while i <= length:
            if array_of_operands[i] in ["+", "-", "*", "/"]:
                operation = array_of_operands[i]
                operand_a = float(array_of_operands[i - 2])
                operand_b = float(array_of_operands[i - 1])
                del array_of_operands[i - 2:i + 1]
                length = len(array_of_operands)

                if operation == "+":
                    sum = operand_a + operand_b
                    array_of_operands.insert(i - 2, sum)
                if operation == "-":
                    diff = operand_a - operand_b
                    array_of_operands.insert(i - 2, diff)
                if operation == "*":
                    product = operand_a * operand_b
                    array_of_operands.insert(i - 2, product)
                if operation == "/":
                    quotient = operand_a / operand_b
                    array_of_operands.insert(i - 2, quotient)
                i = 0
                continue
            i += 1
        return round(array_of_operands[0], 2)


# Takes in the input and output file locations, creates an instance of the PostfixEquation
# class to solve the equation, and saves the solutions to the output file
def main(input_file_loc, output_file_loc):
    input_file = open(input_file_loc, 'r')
    equations = input_file.readlines()
    output_file = open(output_file_loc, 'w')

    for equation in equations:
        postfix_equation = PostfixEquation(equation)
        output_file.write(str(postfix_equation.solution))
        output_file.write("\n")

    output_file.close()


# Takes in a file of postfix equations and outputs the solutions
main("input.txt", "output.txt")
