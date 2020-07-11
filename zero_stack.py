class Stack:
    def __init__(self):
        self.__arr = []
        self.__top = 0

    def push(self, item):
        self.__arr.append(item)
        self.__top += 1

    def isEmpty(self):
        if self.__arr == []:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            return False
        else:
            self.__top -= 1
            item = self.__arr[self.__top]
            del(self.__arr[self.__top])

            return item

    def total_sum(self):
        sum = 0
        for num in self.__arr:
            sum += num
        return sum


count = int(input())
stack = Stack()

for _ in range(count):
    num = int(input())

    if num == 0:
        stack.pop()
    else:
        stack.push(num)

print(stack.total_sum())
