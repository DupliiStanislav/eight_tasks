import argparse
import sys


class FibonacciInRange:
    """
    create class with an empty list and low and high to define our range
    """
    def __init__(self, low, high):
        self.low = low
        self.high = high
        if self.low > self.high:
            print('Upper range lower then lower range')
            sys.exit()

    # generator that yield a number in defined range
    @property
    def fib_nums(self):
        x, y = 1, 1
        while x < self.high:
            yield x
            x, y = y, x + y

    # change str method to show a row of numbers separated by commas
    def __repr__(self):
        return ', '.join(str(i) for i in self.fib_nums
                         if i in range(self.low, self.high))


# Validation functions to check if args exist, positive and integers
def is_valid(num1):
    val1 = int(num1)
    if val1 <= 0:
        print('In this program we can output the fibonacci row with specific requirements'
              'to do this u should use positive numbers as integers')
        raise argparse.ArgumentError
    return val1


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Output Fibonacci nums in specific range')
        parser.add_argument('low', type=is_valid, help='lower range')
        parser.add_argument('high', type=is_valid, help='upper range')
        args = parser.parse_args()
        print(FibonacciInRange(args.low, args.high))
        print(str(sum([1 for i in FibonacciInRange(args.low, args.high).fib_nums
                       if i in range(args.low, args.high)])) + ' numbers in this range')
    except argparse.ArgumentError:
        exc = sys.exc_info()[1]
        print(f'Use positive integer numbers, instead of: {exc}')

