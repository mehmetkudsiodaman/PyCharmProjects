# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
from denemeModule import exampleFunc as ef
from AnimalPackage import animal
from AnimalPackage.CatPackage import cat


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    ef()
    animal.info()
#   cat.speak_direct()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(np.zeros((3, 4)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
