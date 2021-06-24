import math
import random


INSTRUCTION_MSG = """This program takes 4 arguments for create a triangle where:
1st arg is the name of your triangle
and three other args are sides of this triangle
all of the arguments have to be separated by commas"""


class NameIsExist(Exception):
    pass


class Triangle:

    """
    Create class Triangle and initialize it's name and three sides
    """

    def __init__(self, name, side1, side2, side3):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def get_square(self):
        # get square for our triangle.
        p = (self.side1 + self.side2 + self.side3) / 2
        s = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return s

    # check if we can create a triangle with such sides
    def is_exist(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 \
                and self.side2 + self.side3 > self.side1:
            return True
        return False


# Check if we have exactly four arguments and float args for sides
def validation(args):
    if len(args) != 4:
        raise ValueError
    if any(float(num) < 0 for num in args[1:]):
        raise ValueError


# main function to implement all of the logic
def main():

    triangles_dct = {}

    while True:

        # get inputs, validation of arguments and catch exceptions
        try:
            print('Set up name and three sides of your triangle separated by commas, please')
            triangle_params = input().split(',')
            validation(triangle_params)
            if triangle_params[0].strip() in triangles_dct:
                triangle_params[0] = triangle_params[0].strip() + str(random.randint(0, 100))
                raise NameIsExist
        except NameIsExist:
            print('This name is already exist, so it will be changed')
        except ValueError:
            print(INSTRUCTION_MSG)
            continue

        # Create our triangle from class Triangle
        triangle = Triangle(triangle_params[0].strip(), float(triangle_params[1]),
                            float(triangle_params[2]), float(triangle_params[3]))

        # If triangle can be constructed we add to our dict
        if triangle.is_exist():
            triangles_dct[triangle.name] = triangle.get_square
        else:
            print(f'Triangle with side: {triangle.side1}, {triangle.side2}, {triangle.side3} does not exist')

        next_ = input('if you want to add another one triangle print - yes')

        # show our triangles
        if next_.lower() != 'yes':
            for e, i in enumerate(sorted(triangles_dct.items(), key=lambda x: -x[1]), start=1):
                print(f'{e}. [{i[0].capitalize()}]: {round(i[1], 2)}')


if __name__ == '__main__':
    main()
