import argparse
import sys


class NaturalNumbersRow:
    """
    create a class
    """
    def __init__(self, upper_range):
        self.upper_range = upper_range

    # change str method to print properly our row of numbers
    def __repr__(self):
        return ', '.join(str(i) for i in self.required_nums)

    # generator to get our nums one by one
    @property
    def required_nums(self):
        num = 1
        while num ** 2 < self.upper_range:
            yield num
            num += 1


# validation func to check if we have positive integers as arguments
def is_valid(value):
    val = int(value)
    if val <= 0 or not val:
        print('In this program we can output the row of natural numbers with specific requirements'
              'to do this u should use positive numbers as integers')
        raise argparse.ArgumentError
    return val


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Output natural numbers row with requirements')
        parser.add_argument('upper_range', type=is_valid, help='upper_range for natural numbers row')
        args = parser.parse_args()
        n = NaturalNumbersRow(args.upper_range)
        print(n)
    except argparse.ArgumentError:
        exc = sys.exc_info()[1]
        print(f'Use positive integer numbers, instead of: {exc}')