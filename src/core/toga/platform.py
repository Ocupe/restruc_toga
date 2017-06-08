import sys
from functools import lru_cache

@lru_cache(maxsize=8)
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