class MarblesBoard:
    def __init__(self, marbles):
        self.marbles = marbles

    def print_board_state(self, *args):
        output = ""
        for marble in self.marbles:
            output += str(marble) + " "
        output += "\t"
        if args:
            output += args[0]
        print(output)

    def switch(self):
        self.marbles[1], self.marbles[0] = self.marbles[0], self.marbles[1]
        self.print_board_state("switch")

    def rotate(self):
        first_marble = self.marbles[0]
        self.marbles.pop(0)
        self.marbles.append(first_marble)
        self.print_board_state("rotate")

    def is_solved(self):
        if all(self.marbles[i] <= self.marbles[i + 1] for i in range(len(self.marbles) - 1)):
            return True
        else:
            return False


class Solver:
    def __init__(self, marbles):
        self.marbles = marbles
        self.board = MarblesBoard(marbles)
        self.board.print_board_state()
        self.num_steps = 0

    def solve(self):
        if self.board.is_solved():
            print("total steps: ", self.num_steps)
            return
        else:
            self.num_steps += 1
            if self.marbles[0] == 0 or self.marbles[1] == 0:
                self.board.rotate()
            elif self.marbles[0] > self.marbles[1]:
                self.board.switch()
            else:
                self.board.rotate()
            self.solve()


def main():
  board_input = input("Please enter the starting positions of the marbles:")
  try:
    board_list = [int(x) for x in  board_input.split(",")]
  except ValueError as err:
    print('Please enter a list of numbers that is comma delimited')
    main()
  board = Solver(board_list)
  board.solve()

main()