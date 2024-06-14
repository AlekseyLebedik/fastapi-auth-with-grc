import typing as t


class Comparator:
    def __init__(
        self,
        comparatorFunction: t.Optional[t.Callable] = None,
    ) -> None:
        self._comparator = (
            comparatorFunction
            if comparatorFunction
            else Comparator.defaultCompareFunction
        )

    @staticmethod
    def defaultCompareFunction(_, a, b) -> int:
        if a == b:
            return 0
        return -1 if a < b else 1

    def equal(self, a, b) -> bool:
        return self._comparator(a, b) == 0

    def lessThan(self, a, b) -> bool:
        return self._comparator(a, b) < 0

    def greaterThan(self, a, b) -> bool:
        return self._comparator(a, b) > 0

    def lessThanOrEqual(self, a, b) -> bool:
        return self.lessThan(a, b) or self.equal(a, b)

    def greaterThanOrEqual(self, a, b) -> bool:
        return self.greaterThan(a, b) or self.equal(a, b)
