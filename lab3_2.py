from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    value: int
    next: Node | None = None


def newhead(node: Node | None, value: int) -> Node:
    """
    Returns a new linked list with value added to the front.
    """
    return Node(value, node)


def append(node: Node | None, value: int) -> Node:
    """
    Returns a new linked list with value added to the end.
    """
    if node is None:
        return Node(value)

    return Node(node.value, append(node.next, value))


def delete(node: Node | None, index: int) -> Node | None:
    """
    Returns a new linked list with the value at index removed.

    Raises IndexError if index is invalid.
    """
    if node is None:
        raise IndexError("Index out of bounds")

    if index == 0:
        return node.next

    return Node(node.value, delete(node.next, index - 1))


def get(node: Node | None, index: int) -> int:
    """
    Returns the value at index.

    Raises IndexError if index is invalid.
    """
    if node is None:
        raise IndexError("Index out of bounds")

    if index == 0:
        return node.value

    return get(node.next, index - 1)


def get_length(node: Node | None) -> int:
    """
    Returns the number of nodes in the linked list.
    """
    if node is None:
        return 0

    return 1 + get_length(node.next)


def insert(node: Node | None, index: int, value: int) -> Node:
    """
    Returns a new linked list with value inserted at index.

    Students:
    - If index is 0, return a new node whose next is the old list
    - Otherwise, recursively rebuild the list until reaching index
    - Raise IndexError if index is invalid
    """
    # TODO: write this function
    pass


# -------------------------------------------------------------------
# Example usage
# -------------------------------------------------------------------
"""
linked_list = Node(4, Node(3, Node(2, None)))
print("linked_list:", linked_list)

list2 = newhead(linked_list, 5)
print("newhead:", list2)

list3 = append(linked_list, 1)
print("append:", list3)

list4 = delete(linked_list, 1)
print("delete index 1:", list4)

print("get index 0:", get(linked_list, 0))
print("get index 2:", get(linked_list, 2))
"""