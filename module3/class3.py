print("in module3 class3")

from module1.class1 import Class1
from module2.class2 import Class2

class Class3:
    def __init__(self):
        print("in Class3")
        Class1()
        Class2()

if __name__ == "__main__":
    Class3()