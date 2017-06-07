import abc


class FactoryInterface(metaclass=abc.ABCMeta):

    @abc.abstractstaticmethod
    def create_button(self, label):
        return 'created btn instance'


