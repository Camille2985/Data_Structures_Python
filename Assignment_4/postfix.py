class PostfixEquation:
    def __init__(self, equation):
        self.equation = equation
        self.solution = self.main()

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


equation = PostfixEquation("4 2 8 / 5 2 + 2 * - +")
print(equation.solution)
