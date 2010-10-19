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

    def __init__(self):
        self.name = self.__class__.__name__

    def run(self):
        """
        Run all the hook methods implemented on the Hook subclass

        If any method throws an exception, the commit will be rejected
        """
        print 'Running hook: %s' % self.name

        try:
            changed_files = [open(file) for file in self.repo.changed_files()]
            self.all_changed_files(changed_files)
            for file in changed_files:
                self.each_changed_file(file)
        except Exception, e:
            print "\n--- REJECTED ---\n"
            print "Your commit was REJECTED by the hook: %s"  % self.name
            error_message = str(e)
            if error_message:
                print error_message
            sys.exit(1)

    def all_changed_files(self, files):
        pass

    def each_changed_file(self, file):
        pass
