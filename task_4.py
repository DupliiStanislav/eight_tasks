

class FileParser:

    @staticmethod
    def counter_for_string(filepath=None, string=None):
        with open(filepath, 'r', encoding='UTF-8') as f:
            data = f.read()
            if data.count(string) > 0:
                print(f'This file contains {data.count(string)} "{string}"')
            else:
                print(f"This string doesn't exist in this file")

    @staticmethod
    def change_string(filepath=None, string=None, change=None):
        with open(filepath, 'r+', encoding='UTF-8') as f:
            new_data = ''
            data = f.readlines()
            for line in data:
                new_data += line.replace(string, change)

        with open(filepath, 'w', encoding='UTF-8') as f:
            f.write(new_data)

        return print(f'All of the "{string}" are changed to "{change}"')


class Handler:

    @staticmethod
    def validation(string, change=None):
        if string == '' or change == '':
            print('You entered empty strings')

    @staticmethod
    def start():
        while True:
            start = input('If you want to read file and count\n \
any string press 1 if you want to change file press 2\n \
if you want to quit print any key: ')
            try:
                if start == '1':
                    filepath = input('Print the path of yours file: ')
                    string = input('Print the string for count: ')
                    Handler.validation(string)
                    FileParser.counter_for_string(filepath, string)
                elif start == '2':
                    filepath = input('Print the path of yours file: ')
                    string = input('Print the string you want to change: ')
                    change = input('Print the string you want to replace with: ')
                    Handler.validation(string, change)
                    FileParser.counter_for_string(filepath, string)
                    FileParser.change_string(filepath, string, change)
                else:
                    return
            except FileNotFoundError:
                print("Can't find the file check the path, please")
                continue
            except PermissionError:
                print("Can't find the file check the path, please")
                continue


if __name__ == '__main__':
    Handler.start()

