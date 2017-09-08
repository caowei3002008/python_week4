class addAndSub(object):
    def __init__(self, num=0):
        self.num = num

    def add(self, *args):
        for arg in args:
            if type(arg) is int:
                self.num += arg
            else:
                list_add = 0
                for index in range(0,len(arg)):
                    list_add += arg[index]
                self.num += list_add
        return self

    def subtract(self, *argv):
        for arg in argv:
            if type(arg) is int or type(arg) is float:
                self.num -= arg
            else:
                list_sub = 0
                for index in range(0,len(arg)):
                    list_sub += arg[index]
                self.num -= list_sub
        return self

    def print_result(self):
        print self.num
        return self


md = addAndSub()
md.add([1], 3,4).add((3,5,7,8), (2,4.3,1.25)).subtract(2, [2,3], (1.1,2.3)).print_result()

