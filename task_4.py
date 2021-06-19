INSTRUCTION_MSG = ('If you want to read file and count'
                   'any string press 1\nif you want to change file press 2\n'
                   'if you want to quit print any key: ')

FILE_PATH_MSG = 'Print the path of your file: '

ERROR_FIND_MSG = "Can't find the file check the path, please"


class File:
    """
    Create class file
    """
    def __init__(self, path=None):
        self.path = path

    @property
    def get_data(self):
        # read and return data from file
        with open(self.path, 'r', encoding='UTF-8') as f:
            data = f.read()
        return data

    def save_data(self, new_data):
        # save new or changed data to file
        with open(self.path, 'w', encoding='UTF-8') as f:
            f.write(new_data)


class FileHandler:
    """
    Create class FileHandler to manage our files
    """
    def __init__(self, data=None, string=None, change=None):
        self.data = data
        self.string = string
        self.change = change

    def counter_for_string(self):
        # count a number of substrings in file data
        if self.data.count(self.string) > 0:
            print(f'This file contains {self.data.count(self.string)} "{self.string}"')
        else:
            print(f"This string does not exist in this file")
        return self.data.count(self.string)

    def change_string(self):
        # change one substring to other in file data
        new_data = ''
        for line in self.data:
            new_data += line.replace(self.string, self.change)
        return new_data

    def ask_save_new_data(self, file):
        # save changes if we want to
        what = input('If you want to save changes in your file print'
                     '"yes"\nor any key to start again')
        if what.lower() == 'yes':
            file.save_data(self.change_string())


def validation(string=None, change=None):
    # validation if input is None
    if string == '' or change == '':
        print('You entered empty strings')


def main():
    # main function to manage all of the logic
    while True:
        start = input(INSTRUCTION_MSG)
        try:
            if start == '1':
                filepath = input(FILE_PATH_MSG)
                file = File(filepath)
                string = input('Print the string for count: ')
                validation(string)
                handler = FileHandler(file.get_data, string)
                handler.counter_for_string()
            elif start == '2':
                filepath = input(FILE_PATH_MSG)
                file = File(filepath)
                string = input('Print the string you want to change: ')
                change = input('Print the string you want to replace with: ')
                validation(string, change)
                handler = FileHandler(file.get_data, string, change)
                handler.change_string()
                print(f'You have changed {handler.counter_for_string()} substrings'
                      f' {handler.string} to {handler.change}')
                handler.ask_save_new_data(file)
            else:
                return
        except FileNotFoundError:
            print(ERROR_FIND_MSG)
            continue
        except PermissionError:
            print(ERROR_FIND_MSG)
            continue


if __name__ == '__main__':
    main()
