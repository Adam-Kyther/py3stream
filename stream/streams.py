from abc import ABC, abstractmethod


class StreamBase(ABC):

    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.lazy_actions = []

    def get_lazy(self):
        return self.lazy_actions[-1] if len(self.lazy_actions) > 0 else (self.iterable_object.items() if isinstance(self.iterable_object, dict) else self.iterable_object)

    def add(self, generator):
        self.lazy_actions.append(generator)

    def get_first(self, default_value=None):
        return next(self.__iter__(), default_value)

    def __iter__(self):
        yield from self.get_lazy()

    def operations(self):
        return self.lazy_actions

    @abstractmethod
    def filter(self, func):
        pass

    @abstractmethod
    def map(self, func):
        pass

    @abstractmethod
    def fmap(self, func):
        pass

    @abstractmethod
    def to_list(self):
        pass

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def reverse(self):
        pass

    @abstractmethod
    def limit(self, limit):
        pass


class Stream(StreamBase):

    def __init__(self, value):
        super().__init__(value)

    def filter(self, func):
        self.add((i for i in self.get_lazy() if func(i)))
        return self

    def map(self, func):
        self.add((func(i) for i in self.get_lazy()))
        return self

    def fmap(self, func):
        def _wrap(streams):
            for elements in (s.iterable_object for s in streams):
                yield from elements

        self.add(_wrap((func(i) for i in self.get_lazy())))
        return self

    def to_dict(self):
        raise NotImplementedError("Method is not implemented for Stream. Use Dictstream instead.")

    def to_list(self):
        return [e for e in self.get_lazy()]

    def limit(self, limit):
        def _wrap(gen):
            for i, e in enumerate(gen):
                if i < limit:
                    yield e
                else:
                    break
        self.add(_wrap(self.get_lazy()))
        return self

    def reverse(self):
        return reversed(self.to_list())

    def joining(self, delimiter):
        return delimiter.join(self.get_lazy())

    def map_to_str(self):
        return self.map(lambda x: str(x))

    def map_to_int(self):
        return self.map(lambda x: int(x))

    def map_to_float(self):
        return self.map(lambda x: float(x))

    def count(self):
        counter = 0
        for _ in self.get_lazy():
            counter += 1
        return counter

    def any_match(self, func):
        return any(func(i) for i in self.get_lazy())

    def all_match(self, func):
        return all(func(i) for i in self.get_lazy())

    def sum(self):
        return sum(self.get_lazy())

    def max(self):
        return max(self.get_lazy())

    def min(self):
        return min(self.get_lazy())

    def even(self):
        return self.filter(lambda x: x%2 == 0)

    def odd(self):
        return self.filter(lambda x: (x%2 - 1) == 0)

    def gt(self, value):
        return self.filter(lambda x: x > value)

    def lt(self, value):
        return self.filter(lambda x: x < value)

    def ge(self, value):
        return self.filter(lambda x: x >= value)

    def le(self, value):
        return self.filter(lambda x: x <= value)

    def eq(self, value):
        return self.filter(lambda x: x == value)

class IntStream(Stream):
    def __init__(self, start: int, end: int, step: int = 1):
        super().__init__(range(start, end, step))


class DictStream(StreamBase):

    def __init__(self, value: dict):
        super().__init__(value)

    def filter(self, func):
        self.add((k, v) for k, v in self.get_lazy() if func(k, v))
        return self

    def map(self, func):
        self.add((func(k, v) for k, v in self.get_lazy()))
        return self

    def fmap(self, func):
        def _wrap(streams):
            for pairs in (s.iterable_object for s in streams):
                yield from pairs

        self.add(_wrap((func(k,v) for k,v in self.get_lazy())))
        return self

    def to_list(self):
        raise NotImplementedError("Method is not implemented in DictStream. use Stream instead")

    def to_dict(self):
        return {k:v for k,v in self.get_lazy()}

    def items(self):
        return self.__iter__()

    def values(self):
        return Stream((v for _, v in self.get_lazy()))

    def keys(self):
        return Stream((k for k, _ in self.get_lazy()))

    def limit(self, limit):
        pass

    def reverse(self):
        raise NotImplementedError("Method cannot be implemented in dict, because of no order")

