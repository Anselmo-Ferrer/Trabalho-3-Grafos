class _Node:
    def __init__(self, item, next_node):
        self.item = item
        self.next = next_node


class _LinkIterator:
    def __init__(self, current):
        self.current = current

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration()
        item = self.current.item
        self.current = self.current.next
        return item


class Bag:
    def __init__(self):
        self.first = None
        self.n = 0

    def __str__(self):
        return " ".join(str(i) for i in self)

    def __iter__(self):
        return _LinkIterator(self.first)

    def size(self):
        return self.n

    def is_empty(self):
        return self.first is None

    def add(self, item):
        oldfirst = self.first
        self.first = _Node(item, oldfirst)
        self.n += 1
