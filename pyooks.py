import subprocess
import sys

class RepositoryEnvironment(object):
    """
    Provide an interface to a Git repository
    """

    def _run_command(self, args):
        """
        Run a git command.

        args should contain a list of arguments
        that will be appended to the basic git
        command.
        """
        git = subprocess.Popen(['git'] + args, stdout=subprocess.PIPE)
        return git.stdout.read().split('\n')[:-1]

    def changed_lines(self):
        pass

    def changed_files(self):
        return self._run_command(['diff-index', '--cached', '--name-only', 'HEAD'])


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
        print 'Running hook: %s' % self.__class__.__name__

        try:
            changed_files = [open(file) for file in self.repo.changed_files()]
            self.all_files(changed_files)

            for file in changed_files:
                self.each_file(file)
        except Exception, e:
            print e
            sys.exit(1)


    def all_files(self, files):
        pass

    def each_file(self, file):
        pass

    def each_line(self, line):
        pass


if __name__ == '__main__':

    class TestClass(Hook):

        def each_file(self, file):
            print file

