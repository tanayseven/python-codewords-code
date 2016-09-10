class Cart(object):

    def __init__(self):
        self.__items__ = {}

    def is_empty(self):
        return self.size() == 0

    def add_item(self, item):
        if item in self.__items__:
            self.__items__[item] += 1
        else:
            self.__items__[item] = 1

    def size(self):
        return sum(map(self.__items__.get, self.__items__))

    def remove_item(self, item):
        if item not in self.__items__:
            raise CannotRemoveFromCart
        self.__items__[item] -= 1
        if self.__items__[item] == 0:
            self.__items__.pop(item)

    def count_of(self, item):
        return self.__items__[item]

    def exists(self, item):
        return item in self.__items__


class CannotRemoveFromCart(Exception):
    pass