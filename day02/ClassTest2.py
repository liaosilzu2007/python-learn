class Student(object):
    def __init__(self, name, score):
        # 属性名前加__后，属性不能直接访问
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # 可以定义get方法，通过方法来访问
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('Bart Simpson', 59)
# print(bart.__name)
print(bart.get_name())
