#!/usr/bin/python3

"""Define a class for singly linked list"""


class Node:
    """A class that represents node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Inizialize a node

        Args:
            data (int): The node's data
            next_node (Node): the 'next' of the newly created node
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the Node's data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node

        Args:
            value (int): the data of the node
        Raises:
            TypeError: if data is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node of the node that was created"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the new node

        Args:
            value (Node): the next node of the new node
        Raises:
            TypeError: if value is not a Node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be an Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that represents a singly linked list"""

    def __init__(self):
        """
        Initializes a singly linked list
        """
        self.__head = None

    def __str__(self):
        """
        sets the way the print() is represented in the singly linked list
        """
        nodes = []
        current = self.__head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new node into the sorted singly linked list

        Args:
            value (Node): node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    value >= current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
