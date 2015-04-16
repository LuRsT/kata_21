class Node(object):

    next_node = None

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


class List(object):

    first_node = None

    def add(self, value):
        if self.first_node:
            self._get_last_node().next_node = Node(value)
        else:
            self.first_node = Node(value)

    def find(self, value):
        for node in self:
            if node.get_value() == value:
                return node
        else:
            raise KeyError

    def get_values(self):
        return [v.get_value() for v in self]

    def __iter__(self):
        node = self.first_node
        while node is not None:
            yield node
            node = node.next_node

    def _get_last_node(self):
        for node in self:
            if node.next_node is None:
                return node

    def delete(self, value):
        if self.first_node.get_value() == value:
            self.first_node = self.first_node.next_node
            return

        previous_node = self.first_node
        node = self.first_node.next_node
        while node is not None:
            if node.get_value() == value:
                previous_node.next_node = node.next_node or None
                return
            previous_node = node
            node = node.next_node
