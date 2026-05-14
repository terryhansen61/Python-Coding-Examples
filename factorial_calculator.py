import os

def clear_screen():
    """This clears the output screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def factorial(n):
    """Checks to see if the input number is valid, must be greater than zero.
        Then is does the factorial which is the input number times the
        same number (i.e., 5 = 5*4*3*2*1 = 120"""
    if n < 0:
        return 'Factorial not defined for negative numbers'

    results = 1

    for i in range(1, n+1):
        results *= i

    return results

def run_factorial_calculator():
    """This runs the factorial calculator"""
    while True:
        clear_screen()
        print('Factorial Calculator')
        print('Type ''exit'' to quit the program')

        user_input = input('\nEnter a number: ')

        if user_input.lower() == 'exit':
            print('\nGoodbye!')
            break

        if not user_input.lstrip('-').isdigit():
            print('\nPlease enter a valid number')
            input('\nPress enter to continue...')
            continue

        n = int(user_input)
        print(f'\nFactorial of {n} is: {factorial(n)}')
        input('\nPress enter to continue...')

if __name__ == '__main__':
    run_factorial_calculator()

