import typing as t

from loguru import logger

T = t.TypeVar("T")


class Queue(t.Generic[T]):
    def __init__(self) -> None:
        from .linked_link import LinkedList

        self.items = LinkedList()

    def isEmpty(self):
        return not bool(self.items.head)

    def peek(self):
        if self.isEmpty():
            return None

        return self.items.head.value

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        removedHead = self.items.deleteHead()
        return removedHead if removedHead.value else None

    def toString(self, callback):
        return self.items.toString(callback)
