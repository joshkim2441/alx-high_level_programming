#!/usr/bin/python3
"""Define class for a singly_linked list"""


class Node:
    """represents a singly_linked list node"""

    def __init__(self, data, next_node=None):
        """initialize a new node

        Args:
            data (int): the data of the new node
            next_node (Node): the next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get/set the data of the Node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get/set the next node of the Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """represents a singly_linked list"""

    def __init__(self):
        """initialize a new singly_linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new node to the singly_linked list

        the node is inserted into the list at the
        correct ordered numerical position

        Args:
            value (Node): the new Node to be inserted
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node

    def __str__(self):
        """define print() representation of a singly linked list"""
        node = self.__head
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return ("\n".join(result))
