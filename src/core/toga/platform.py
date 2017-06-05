# defines which platform toga is running on
import sys
import os


# from .factory import Factory



class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Platform(object):
    __metaclass__ = Singleton

    def __init__(self, platform=None):
        self.platform_name = None
        self._factory = self.get_platform_factory()

    @property
    def factory(self):
        return self._factory

    @factory.setter
    def factory(self, factory):
        self._factory = factory

    def get_platform_factory(self):
        if self.platform_name is None:
            if sys.platform == 'ios':
                self.platform_name = 'iOS'
            elif sys.platform == 'tvos':
                self.platform_name = 'tvOS'
            elif sys.platform == 'watchos':
                self.platform_name = 'watchOS'
            elif sys.platform == 'android':
                self.platform_name = 'android'
            elif sys.platform == 'darwin':
                self.platform_name = 'cocoa'
                from toga_cocoa.toga_cocoa_factory import TogaCocoaFactory
                self.factory = TogaCocoaFactory
            elif sys.platform == 'linux':
                self.platform_name = 'gtk'
            elif sys.platform == 'win32':
                self.platform_name = 'winforms'
            else:
                raise RuntimeError("Couldn't identify a supported host platform.")
        return self.factory


# def get_platform():
#     factory = get_platform_name()
#     # for sc in Factory.__subclasses__():
#     #     print(sc.__name__)
#     return 'cocoa'
#
#
# def get_platform_factory():
#     factory = None
#
#     def wrapped():
#         nonlocal factory
#         if factory:
#             return factory
#         else:
#             platform_name = os.environ.get('TOGA_PLATFORM')
#
#             # If we don't have a manually defined platform, attempt to
#             # autodetect and set the platform
#             if platform_name is None:
#                 if sys.platform == 'ios':
#                     platform_name = 'iOS'
#                 elif sys.platform == 'tvos':
#                     platform_name = 'tvOS'
#                 elif sys.platform == 'watchos':
#                     platform_name = 'watchOS'
#                 elif sys.platform == 'android':
#                     platform_name = 'android'
#                 elif sys.platform == 'darwin':
#                     platform_name = 'cocoa'
#                     from toga_cocoa.toga_cocoa_factory import TogaCocoaFactory
#                     factory = TogaCocoaFactory
#                 elif sys.platform == 'linux':
#                     platform_name = 'gtk'
#                 elif sys.platform == 'win32':
#                     platform_name = 'winforms'
#                 else:
#                     raise RuntimeError("Couldn't identify a supported host platform.")
#             return factory
#
#     return wrapped
