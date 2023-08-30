#!/usr/bin/python3
"""
Node Class

This script defines a class for representing a node.
"""


class Node:
    """

    Node class for a singly linked list.
    """

    @property
    def data(self):
        """

        Retrieve the data stored in the Node.
        """
        return self.__data

    @property
    def next_node(self):
        """

        Retrieve the next Node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """

        Set the next Node in the linked list.
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.
                                                                    Args:
            data: The data to be stored in the Node.
            next_node (Node, optional): The next Node in the linked list.
                                       Defaults to None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    SinglyLinkedList class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.

        Args:
            value: The data to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (
                current.next_node is not None and
                current.next_node.data < value
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """

        Print the entire list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)
