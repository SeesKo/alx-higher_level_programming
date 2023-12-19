#!/usr/bin/python3
"""Defining a class node"""


class Node:
    """A class representing a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new instance of the Node class.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the linked list.
            Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method for retrieving the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method for setting the data of the node.

        Args:
            value (int): The data of the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method for retrieving the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method for setting the next node in the linked list.

        Args:
            value (Node): The next node in the linked list or None.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        """Initialize a new instance of the SinglyLinkedList class.

        The linked list is represented by its head.
        """
        self.head = None

    def __str__(self):
        """Return a string representation of the linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data)
            current = current.next_node
            if current:
                result += "\n"
        return result

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list
        (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
