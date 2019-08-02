class Stack():
    """
    以list为基础实现的栈
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            print("栈为空")
            return
        return self._data.pop()

    def top(self):
        if self.is_empty():
            print("栈为空")
            return
        return self._data[-1]

    def travel(self):
        for i in range(0, len(self._data)):
            print("%d" % self._data[i])


if __name__ == '__main__':
    print("创建栈")
    stack = Stack()
    stack.pop()
    print("验证是否为空:", end="")
    empty = stack.is_empty()
    if empty == True:
        print("空栈")
    else:
        print("不是空")
    print("进栈")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print("遍历验证进栈")
    stack.travel()
    print("判断是否为空：", end=" ")
    empty = stack.is_empty()
    if empty == True:
        print("空栈")
    else:
        print("不是空")
    print("出栈:", end=" ")
    pop = stack.pop()
    print(pop)
    stack.travel()
    print("验证栈顶元素：", end=" ")
    top = stack.top()
    print(top)