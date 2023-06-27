#!/usr/bin/python3

class Node:
    """Node class for a singly linked list."""
    def __init__(self, data, next_node=None):
        """Node constructor.
        Args:
            data (int): Data stored in the node.
            next_node (Node, optional): Next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        """Get the data stored in the node."""
        return self._data
    @data.setter
    def data(self, value):
        """Set the data stored in the node.
        Args:
            value (int): Data to store in the node.
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value
    @property
    def next_node(self):
        """Get the next node in the list."""
        return self._next_node
    @next_node.setter
    def next_node(self, value):
        """Set the next node in the list.
        Args:
            value (Node): Next node in the list.
        Raises:
            TypeError: If value is not a Node object.
        """
        if not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value

class SinglyLinkedList:
    """Singly linked list class."""
    def __init__(self):
        """Singly linked list constructor."""
        self.head = None
    def __str__(self):
        """String representation of the list."""
        node = self.head
        while node:
            print(node.data)
            node = node.next_node
        return ""
    def sorted_insert(self, value):
        """Insert a new node into the list in the correct sorted position.
        Args:
            value (int): Data to store in the new node.
        """
