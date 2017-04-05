

"""
    Usage:
        search <your_query>
"""

from docopt import docopt,DocoptExit
from functions import GoogleSearchApi as gsa
import cmd
import os
from termcolor import colored,cprint
from prettytable import *



def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    os.system("clear")
    print(__doc__)


class GSA(cmd.Cmd):
    text = colored('GSA$$$', 'green', attrs=['blink'])
    prompt = text

    @docopt_cmd
    def do_search(self, arg):
        """Usage: search <your_query>"""
        search_term=arg['<your_query>']
        search_data=gsa.search(search_term)
        kind_data=search_data['kind']
        queries_data=search_data['queries']
        search_info=search_data['searchInformation']
        items_data=search_data['items']
        heading=PrettyTable(['Heading'])
        heading.add_row([kind_data])
        heading.add_row(['Total Results : '+queries_data['request'][0]['totalResults']])
        print(heading)
        print()
        for item in items_data:
            item_title=item['title']
            data_table=PrettyTable([item_title])
            data_table.add_row([item['kind']])
            data_table.add_row([item['snippet']])
            data_table.add_row([item['link']])
            print(data_table)
            print()

    @docopt_cmd
    def do_quit(self, arg):
        """Usage: quit"""
        os.system('clear')
        print ('GSA has quit')
        exit()


if __name__ == "__main__":
    try:
        intro()
        GSA().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('GSA has quit')
