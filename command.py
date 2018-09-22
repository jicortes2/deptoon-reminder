from random import choice
from db import add_element
from datetime import datetime
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
        **Use:** /reminder periodicity date message
        **Example:** /reminder monthly 22-11 This message will be sent on every 22nd
        **Periodicity options:** once, monthly, annually
    """
    # /reminder once 23-06 hola!
    if args.count(' ') < 2:
        return reminder.__doc__
    frequency, date_string, msg = args.split(' ', 2)
    periodicity = TYPES[frequency.lower()]
    date = datetime.strptime(date_string, '%d-%m')
    if db.add_element(chat_id, periodicity, date, msg):
        return args, chat_id
    else:
        return periodicity, date, msg, chat_id

# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Default answer for wrong commands """
    return "The command {} doesn't exists".format(command)
