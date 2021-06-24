import tkinter as tk
from tkinter import messagebox as msg

# dictionary with keys ints nums and values string equals
NUMBERS = {
    1: ('один', 'одна'),
    2: ('два', 'две'),
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восем',
    9: 'девять',
    10: 'десять',
    11: 'одинадцать',
    12: 'двенадцать',
    13: 'тринадцать',
    14: 'четырнадцать',
    15: 'пятнадцать',
    16: 'шестнадцать',
    17: 'семнадцать',
    18: 'восемнадцать',
    19: 'девятнадцать',
    20: 'двадцать',
    30: 'тридцать',
    40: 'сорок',
    50: 'пятьдесят',
    60: 'шестьдесят',
    70: 'семьдесят',
    80: 'восемьдесят',
    90: 'девяносто',
    100: 'сто',
    200: 'двести',
    300: 'триста',
    400: 'четыреста',
    500: 'пятсот',
    600: 'шестьсот',
    700: 'семьсот',
    800: 'восемьсот',
    900: 'девятьсот',
}

# store cases for thousands name
THOUSANDS = ('тысяча', 'тысячи', 'тысяч')

# store cases for millions name
MILLIONS = ('миллион ', 'миллиона ', 'миллионов ')


class NumToString:
    """
    Create a class NumToString
    """
    def __init__(self, num):
        self.num = num

    # method to return string name of a number
    @staticmethod
    def get_name(num, case=None):

        name = ''
        val = num
        div = 1000

        while val:
            cur = int(val - (val % div))

            if cur <= 0:
                div /= 10
                cur = int(val - (val % div))
                if case == 'thousand':
                    if cur > 0 and val > 19:
                        name += ''.join(NUMBERS[cur][1] + ' ' if cur <= 2 else NUMBERS[cur] + ' ')
                    elif cur > 0 and val < 20:
                        name += ''.join(NUMBERS[val][1] + ' ' if cur <= 2 else NUMBERS[val] + ' ')
                        break
                else:
                    if cur > 0 and val > 19:
                        name += ''.join(NUMBERS[cur][0] + ' ' if cur <= 2 else NUMBERS[cur] + ' ')
                    elif cur > 0 and val < 20:
                        name += ''.join(NUMBERS[val][0] + ' ' if cur <= 2 else NUMBERS[val] + ' ')
                        break
            else:
                name += NUMBERS[cur] + ' '

            val = int(val % div)

        return name

    # method to get proper name for millions and thousands
    @property
    def get_proper_name(self):

        val = abs(self.num)
        thousands = int(val // 1000)
        millions = int(val // 1000000)

        if str(thousands)[-1] == '1':
            name_t = THOUSANDS[0]
        elif str(thousands)[-2:] not in ['12', '13', '14'] and str(thousands)[-1] in '234':
            name_t = THOUSANDS[1]
        else:
            name_t = THOUSANDS[2]

        if millions > 0:

            thousands = int(val % 1000000 // 1000)

            if str(millions)[-1] == '1':
                name_m = MILLIONS[0]
            elif str(millions)[-2:] not in ['12', '13', '14'] and str(millions)[-1] in '234':
                name_m = MILLIONS[1]
            else:
                name_m = MILLIONS[2]

            return (name_t if thousands > 0 else ''), name_m
        return name_t if thousands > 0 else ''

    # final method to stick all of the stings to create the name of a number
    def get_string(self):
        name = ''
        val = abs(self.num)

        if self.num < 0:
            name += 'минус '

        if val < 1000000:
            thousands = int(val // 1000)
            numbers = int(val % 1000)
        else:
            millions = int(val // 1000000)
            thousands = int(val % 1000000 // 1000)
            numbers = int(val % 1000000 % 1000)
            name += self.get_name(millions) + self.get_proper_name[1] + \
                    self.get_name(thousands, 'thousand') + self.get_proper_name[0] + \
                    ' ' + self.get_name(numbers)

            return name

        if val == 0:
            return 'Ноль'
        elif thousands > 0:
            name += self.get_name(thousands, 'thousand') + self.get_proper_name \
                    + ' ' + self.get_name(numbers)
        else:
            name += self.get_name(numbers)

        return name


class GUI:
    """
    Create class GUI to initialize interface representation
    """
    def __init__(self, root):
        self.root = root
        self.inputs = tk.Entry(self.root, width=30, justify='center', font=20, bd=5)
        self.inputs.pack()
        self.btn_get_string = tk.Button(text='Get info', width=15, height=3, command=self.instructions)
        self.btn_get_string.pack()
        self.btn_get_string = tk.Button(text='Get string', width=15, height=3, command=self.show_string)
        self.btn_get_string.pack()
        self.results = tk.Label(self.root, text='string:', height=5, font=5)
        self.results.pack()

    # method for button click representation and makes a string name of a given number
    def show_string(self):
        try:
            nts = NumToString(int(self.inputs.get()))
            text = nts.get_string()
            self.results.config(text=text)
        except ValueError:
            self.error_msg_value()
        except KeyError:
            self.error_msg_key()

    # error message representation in GUI
    @staticmethod
    def error_msg_value():
        msg.showerror('Error', 'Use integers')

    # error message representation in GUI
    @staticmethod
    def error_msg_key():
        msg.showerror('Error', 'this program works till one billion')

    # show message with instructions for our program
    @staticmethod
    def instructions():
        msg.showinfo('Info', 'This program can convert you integer input '
                             'to string output, you can use negative numbers as well')


if __name__ == '__main__':
    root = tk.Tk()
    gui = GUI(root=root)
    root.mainloop()
