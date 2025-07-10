#!/usr/bin/python3
"""
Defines a singly linked list with sorted insertion.
"""

class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data  # validated by setter
        self.next_node = next_node  # validated by setter

    @property
    def data(self):
        """Retrieve the data value."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data value, must be int."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, must be None or Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """Print the list one node's data per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node with value in sorted order (increasing)."""
        new_node = Node(value)
        # Special case: empty list or new value should be new head
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Otherwise, find correct insertion point
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        # Insert new_node after current
        new_node.next_node = current.next_node
        current.next_node = new_node

