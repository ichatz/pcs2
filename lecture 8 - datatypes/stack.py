import sys

class StackError(Exception):

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class Stack(object):

    def __init__(self, size):
        self.content = []
        self.size = size
        self.min = [sys.maxsize]

    def mySize(self):
        return len(self.content)

    def isEmpty(self):
        return not bool(self.content)

    def push(self, value):
        if (self.mySize() >= self.size):
            raise StackError(self,"full")

        if (value < self.min[0]):
            self.min.insert(0, value)
        else:
            self.min.insert(0, self.min[0])

        self.content.insert(0, value)

    def pop(self):
        if (self.isEmpty()):
            raise StackError(self, "empty")

        value = self.content.pop(0)
        self.min.pop(0)

        return value

    def min(self):
        return self.min[0]

    def minOld(self):
        min = type(sys.maxsize)
        for x in self.content:
            if x < min:
                min = x

        return min

    def min2(self):
        return min(self.content)

if __name__ == '__main__':

    q = Stack(5)
    print(q.mySize())

    if (q.isEmpty()):
        print("Stack is empty")

    try:
        for x in range(0, 6):
            print("PUSH", x)
            q.push(x)
            print("Stack size", q.mySize())

    except StackError:
        print("Stack full")

    for x in range(0,6):
        print("POP")
        v = q.pop()
        print(v, " - Stack size", q.mySize())