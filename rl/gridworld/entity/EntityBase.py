import abc


class EntityBase(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def can_interact(self, other):
        pass

    # @property
    @abc.abstractmethod
    def character(self):
        pass

