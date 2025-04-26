class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

    def read(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None
