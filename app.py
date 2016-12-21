#!/usr/bin/env python
"""
This Application uses docopt with the built in cmd module to employ an
interactive command application.
Usage:
    amity tcp <host> <port> [--timeout=<seconds>]
    amity serial <port> [--baud=<n>] [--timeout=<seconds>]
    amity (-i | --interactive)
    amity (-h | --help | --version)
    amity create_room <room_name>
    amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
    amity reallocate_person <person_identifier> <new_room_name>
    amity load_people <filename>
    amity print_unallocated [--o=filename.txt]
    amity print_allocations [--o=filename.txt]
    amity print_room <room_name>
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from models.amity import Amity
from pyfiglet import Figlet,figlet_format
from termcolor import cprint


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    f = Figlet(font = 'bubble')
    print(cprint(figlet_format("Hello!", font = 'broadway'),'cyan'))
    print('******************************************')
    intro = 'Welcome to the Amity Room Allocation Application!' \
        + ' (type help for a list of commands.)'
    prompt = '(amity) '
    file = None
    amity = Amity()

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name>"""
        pass

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
        """
        pass

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """Usage: reallocate_person <person_identifier> <new_room_name>
        """
        pass

    @docopt_cmd
    def do_load_people (self, arg):
        """Usage: load_people <filename>
        """
        pass

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [--o=filename.txt]
        """
        pass

    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [--o=filename.txt]
        """
        pass

    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>
        """
        pass

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('************************')
        print('Thank you! Good Bye!')
        print('************************')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
