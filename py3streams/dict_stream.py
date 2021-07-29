
from .stream_base import StreamBase
from .stream import Stream


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

