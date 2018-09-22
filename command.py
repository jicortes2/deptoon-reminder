from random import choice
from db import add_element
import os


TOKEN = str(os.environ['TOKEN'])
TYPES = {
    'once': 0,
    'monthly': 1,
    'annually': 2
}
# Public commands

def start(sender_id, command):
    return "Deptoon Reminder at your service"

def reminder(chat_id, command, args):
    """
        Add a reminder to your chat
        Use: /reminder periodicity date message
        Example: /reminder monthly 22-11 This is an example
        Periodicity options: once, monthly, annually
    """
    # /reminder once 23-06 hola!
    if args.count(' ') < 3:
        return reminder.__doc__
    frequency, date, msg = args.split(' ', 2)
    periodicity = TYPES[frequency.lower()]
    return args

# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Default answer for wrong commands """
    return "The command {} doesn't exists".format(command)
