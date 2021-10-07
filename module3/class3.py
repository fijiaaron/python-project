print("in file: " + __file__)

from module1.class1 import Class1
from module2.class2 import Class2

class Class3:
    def __init__(self):
        print("initializing Class3")
        Class1()
        Class2()

if __name__ == "__main__":
    Class3()