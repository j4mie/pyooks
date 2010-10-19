Pyooks
======

**Declarative [Git Hooks](http://www.kernel.org/pub/software/scm/git/docs/githooks.html) in Python.**

**Pyooks** aims to make it easy to create and maintain Git Hooks, even if you're not a Bash ninja. Hooks are written as simple Python classes, and implement methods to handle changed files, lines, commit messages, etc.

**A early sketch of an idea - NOT ready for use**

An Example Hook
---------------

Put this in `.git/hooks/pre-commit`

    #!/usr/bin/python

    from pyooks import Hook

    class RejectCRLF(Hook):
        def each_changed_file(self, file):
            if "\r\n" in file.read():
                raise Exception

Try to commit a file with some nasty CRLF characters in it:

    $ git commit -am 'Some changes made on Windows'
    Running hook: RejectCRLF

    --- REJECTED ---

    Your commit was REJECTED by the hook: RejectCRLF

Thoughts
--------

This is a very early-stage implementation, and is really just an outline of the idea. Here are a few more thoughts:

* Currently, this version of the code is oriented towards pre-commit hooks, and rejects commits by throwing exceptions.

* Ultimately it needs to deal with any kind of hook. It should be able to inspect and rewrite commit messages, change files, parse information passed from Git on standard input, handle server hooks, deploy code and post commit messages to Twitter.

* Because hooks are just Python, it should be able to accommodate any of these requirements - but the API for interacting with Git and the file system has to be designed correctly and carefully. A good approach might be to port across some existing Bash hooks found around the web and see what kind of API they need.

* It might be useful to have a *contrib* directory containing some example hooks.

* It would be nice if pyooks worked well with [git-hooks](http://github.com/icefox/git-hooks/) ("A tool to manage project, user, and global Git hooks").

* Pyooks should be pronounced "pukes".


Call for contributions
----------------------

I'm pretty sure I'm going to need some help with this. Please fork my code, send me a message on Github, [email me](mailto:jamie.matthews@gmail.com) or open some tickets if you'd like to get involved.
