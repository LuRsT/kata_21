class Node(object):

    def __init__(self, contents):
        self.contents = contents
        self.next_object = None


class List(object):

    first_node = None

    def append(self, value):
        new_node = Node(value)
        if self.first_node is None:
            self.first_node = new_node
        else:
            last_node = self._get_last_node()
            last_node.next_object = new_node

    def _get_last_node(self):
        node = self.first_node
        while node.next_object is not None:
            node = node.next_object
        return node

    def index(self, value):
        if self.first_node is None:
            raise ValueError

        print(self.first_node)
        for index, node_contents in enumerate(self):
            if node_contents == value:
                return index

        raise ValueError

    def delete(self, index):
        if index == 0:
            node = self.first_node
            if node is None:
                raise IndexError
            self.first_node = node.next_object
            del node
            return

        for idx, node in enumerate(self._nodes()):
            if idx == index - 1:
                prev = node
                break
        else:
            return

        node = prev.next_object
        if node is None:
            raise IndexError
        next_node = node.next_object
        prev.next_object = next_node
        del node

    def _nodes(self):
        node = self.first_node
        while True:
            if node is None:
                return

            yield node

            node = node.next_object


    def __iter__(self):
        for node in self._nodes():
            yield node.contents
