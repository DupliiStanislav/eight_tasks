import task_4


class LuckyTickets(task_4.File):

    """
    create class and inherit from the class File
    from task_4 which has get_data and save_data methods
    and attribute self.path for path to file
    """

    # method returns count of all exist tickets and
    # a list with these tickets
    @property
    def get_moscow_lucky_tickets(self):
        counter = 0
        mlt = []
        for i in range(1, 1000000):
            tick = f'{i:06}'
            if sum(map(int, tick[:3])) == sum(map(int, tick[3:])):
                mlt.append(tick)
                counter += 1
        return counter, mlt

    # method returns count of all exist tickets and
    # a list with these tickets
    @property
    def get_piter_lucky_tickets(self):
        counter = 0
        plt = []
        for i in range(1, 1000000):
            tick = f'{i:06}'
            if sum([int(i) for i in tick if int(i) % 2 == 0]) == \
                    sum([int(i) for i in tick if int(i) % 2 != 0]):
                plt.append(tick)
                counter += 1
        return counter, plt


if __name__ == '__main__':
    while True:
        try:
            path = input(task_4.FILE_PATH_MSG)
            lt = LuckyTickets(path)
            what = lt.get_data.lower()
            if what.strip() == 'moscow':
                print(f'There are exist {lt.get_moscow_lucky_tickets[0]} '
                      f'Moscow lucky tickets')
                data = ''
                for e, i in enumerate(lt.get_moscow_lucky_tickets[1]):
                    data += i + ' ' if e % 5 != 0 else '\n' + i + ' '
                LuckyTickets(r'C:\Users\User\Desktop\TASKS\ticketslist.txt').save_data(data)
            elif what.strip() == 'piter':
                print(f'There are exist {lt.get_piter_lucky_tickets[0]} '
                      f'Piter lucky tickets')
                data = ''
                for e, i in enumerate(lt.get_piter_lucky_tickets[1]):
                    data += i + ' ' if e % 5 != 0 else '\n' + i + ' '
                LuckyTickets(r'C:\Users\User\Desktop\TASKS\ticketslist.txt').save_data(data)
        except FileNotFoundError:
            print(task_4.ERROR_FIND_MSG)
            continue
        except PermissionError:
            print(task_4.ERROR_FIND_MSG)
            continue

