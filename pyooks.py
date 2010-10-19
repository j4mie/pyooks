

class RepositoryEnvironment(object):
    """
    Provide an interface to a Git repository
    """
    def changed_lines(self):
        pass

    def changed_files(self):
        pass


class HookMeta(type):
    """
    Metaclass for all hooks.
    """
    def __init__(cls, name, bases, ns):
        """
        Metaclass constructor

        When each hook class is created, this method
        simply creates an instance of the class and
        calls its `run()` method.
        """

        # Only run the hook if this is
        # a subclass of the Hook base class.
        if (object not in bases):
            hook = cls()
            hook.run()


class Hook(object):
    """
    Base class for all Hook classes
    """
    __metaclass__ = HookMeta

    repo = RepositoryEnvironment()

    def run(self):
        print 'running hook %s' % self.__class__.__name__


if __name__ == '__main__':

    class TestClass(Hook):
        pass
