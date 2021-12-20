# Function that returns if player one has a winning streak based on a user
def is_hot(n):
    if n < 1:
        return False
    else:
        return not(is_hot(n - 1)) or not(is_hot(n / 2))

# Converts the boolean return value of is_hot into a readable string
def state(n):
    if is_hot(n):
        return "hot"
    else:
        return "cold"

# Initialize program and controls flow of execution
def main():
    try:
        print("Player 1 is in a ", state(int(input("Starting number:"))))
        return
    except ValueError as err:
        print('Please enter a number value')
        main()

main()