import abc


class FactoryInterface(metaclass=abc.ABCMeta):
    # factory = None


    # def __init__(self, platform=None):
    # if self.factory is None:
    #     # if not platform is provided try to find the right platform
    #     self.platform = platform if platform is not None else get_platform()
    #
    #     if self.platform == 'cocoa':
    #         self.create_cocoa_factory()
    #     else:
    #         raise RuntimeError('Platform: "{}" is not implemented.'.format(self.platform))
    # else:
    #     return self.factory
    # pass



    @abc.abstractmethod
    def create_button(self, label):
        return 'created btn instance'

        # def create_cocoa_factory(self):
        #     self.factory = TogaCocoaFactory()
        #     return self.factory

        # def create_ios_factory(self):
        #     pass
