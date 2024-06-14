import typing as t

from .comparator import Comparator

T = t.TypeVar("T")


class LinkedListNode(t.Generic[T]):

    def __init__(
        self,
        value: T,
        next: t.Optional["LinkedListNode[T]"] = None,
    ) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"LinkedListNode(value={str(self.value)}, next={str(self.next.value)})"


class LinkedList(t.Generic[T]):
    def __init__(self, comperatorFunction) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        self._comperator = Comparator(comperatorFunction)

    def append(self, value: T):
        self.size += 1
        node = LinkedListNode[T](value)

        if self.head is None:
            self.head = node
            self.tail = node
            return self

        self.tail.next = node
        self.tail = node

        return self

    def prepend(self, value: T):
        node = LinkedListNode[T](value, self.head)
        self.head = node

        if not self.tail:
            self.tail = node

        return self

    def insert(self, value: T, rawIndex: int):
        index = rawIndex if rawIndex > 0 else 0

        if index == 0:
            self.prepend(value)
        else:
            count = 1
            currentNode = self.head
            node = LinkedListNode(value)

            while currentNode:
                if count == index:
                    break
                currentNode = currentNode.next
                count += 1

            if currentNode:
                node.next = currentNode
                currentNode.next = node
            else:
                if self.tail:
                    self.tail.next = node
                    self.tail = node
                else:
                    self.head = node
                    self.tail = node

        return self

    def delete(self, value: T):
        if not self.head:
            return None

        deletedNode = None

        while self.head and self._comperator.equal(value, self.head.value):
            deletedNode = self.head
            self.head = self.head.next

        currentNode = self.head

        if not currentNode is None:
            while currentNode.next:
                if self._comperator.equal(currentNode.next.value, value):
                    deletedNode = currentNode.next.value
                    currentNode.next = currentNode.next.next
                else:
                    currentNode = currentNode.next

        if self._comperator(self.tail.value, value):
            deletedNode = self.tail
            self.tail = currentNode

        return deletedNode

    def find(self, value: T, callback: t.Callable = None):
        if not self.head:
            return None

        currentNode = self.head

        while currentNode:
            if callback and callback(currentNode.value):
                return currentNode

            if value and self._comperator.equal(currentNode.value, value):
                return currentNode

            currentNode = currentNode.next

        return None

    def deleteTail(self):
        deletedTail = self.tail

        if self.head == self.tail:
            self.head = self.tail = None

            return deletedTail

        currentNode = self.head

        while currentNode.next:
            if currentNode.next.next:
                currentNode.next = None
            else:
                currentNode = currentNode.next

        self.tail = currentNode

        return deletedTail

    def deleteHead(self):
        if not self.head:
            return None

        deletedHead = self.head

        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        return deletedHead

    def fromList(self, values: t.List[T]):
        for value in values:
            self.append(value)

        return self

    def toList(self):
        values = []

        currentNode = self.head

        while currentNode:
            values.append(currentNode.value)
            currentNode = currentNode.next

        return values

    def toString(self, callback=None):
        values = self.toList()
        return " ".join([callback(value) if callback else value for value in values])
