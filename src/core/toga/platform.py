import sys


def get_platform_factory():
    if sys.platform == 'ios':
        pass
    elif sys.platform == 'tvos':
        pass
    elif sys.platform == 'watchos':
        pass
    elif sys.platform == 'android':
        pass
    elif sys.platform == 'darwin':
        from toga_cocoa.toga_cocoa_factory import TogaCocoaFactory
        return TogaCocoaFactory
    elif sys.platform == 'linux':
        pass
    elif sys.platform == 'win32':
        pass
    else:
        raise RuntimeError("Couldn't identify a supported host platform.")


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Platform(object):
    """ Platform handles stuff like:
    - on what platform does toga run
    - providing the requested or for the system suitable TogaFactory

    """
    __metaclass__ = Singleton

    def __init__(self, platform=None):
        self.platform_name = None
        self._factory = self.get_platform_factory()

    @property
    def factory(self):
        return self._factory

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
                self._factory = TogaCocoaFactory
            elif sys.platform == 'linux':
                self.platform_name = 'gtk'
            elif sys.platform == 'win32':
                self.platform_name = 'winforms'
            else:
                raise RuntimeError("Couldn't identify a supported host platform.")
        return self.factory