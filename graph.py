class Graph:
    def __init__(self):
        self.nodes = []

    def size(self):
        return len(self.nodes)


class Table(Graph):
    def __init__(self, maxNum):
        super().__init__(self)
        self.maxNum = maxNum

    def numSpaces(self):
        return self.maxNum - self.size()