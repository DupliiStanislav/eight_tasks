import random
import tkinter as tk
import unittest
from task_5 import NumToString, NUMBERS, GUI


class TestNumToString(unittest.TestCase):
    """
    test for task 5
    """
    # setup instancies and root
    def setUp(self) -> None:
        self.root = tk.Tk()
        self.events()
        self.ntm1 = NumToString(1)
        self.ntm2 = NumToString(1001)
        self.ntm3 = NumToString(1020001)

    # teardown to shout up the root and events
    def tearDown(self) -> None:
        if self.root:
            self.root.destroy()
            self.events()

    # events mask
    def events(self):
        while self.root.dooneevent(tk._tkinter.ALL_EVENTS | tk._tkinter.DONT_WAIT):
            pass

    # test entry method for GUI
    def test_entry_tk(self):
        gui = GUI(self.root)

        self.events()
        gui.inputs.focus_set()
        gui.inputs.insert(tk.END, '152')
        gui.inputs.event_generate('<Return>')
        self.events()
        self.assertEqual('152', gui.inputs.get())
        num_to_string = NumToString(int(gui.inputs.get()))
        self.assertEqual(num_to_string.get_string(), 'сто пятьдесят два')

    # test get name method for nums
    def test_get_name(self):
        for i in range(10):
            rnd_num = random.randint(1, 20)
            if rnd_num > 2:
                self.assertEqual(self.ntm1.get_name(rnd_num), NUMBERS[rnd_num])
            else:
                self.assertEqual(self.ntm1.get_name(rnd_num), NUMBERS[rnd_num][0])

        self.assertEqual(self.ntm2.get_name(999), 'девятьсот девяносто девять')
        self.assertEqual(self.ntm2.get_name(102), 'сто два')

    # get proper name for thousands and millions
    def test_get_proper_name(self):

        self.assertEqual(self.ntm2.get_proper_name, 'тысяча')
        self.assertEqual(self.ntm3.get_proper_name[1], 'миллион')


if __name__ == '__main__':
    unittest.main()