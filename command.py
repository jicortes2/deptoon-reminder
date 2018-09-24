from random import choice
from db import add_reminder
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
        <strong>Use:</strong> /reminder periodicity date message
        <strong>Example:</strong> /reminder monthly 22-11 This message will be sent on every 22nd
        <strong>Periodicity options:</strong> once, monthly, annually
    """
    # /reminder once 23-06 hola!
    if args.count(' ') < 2:
        return reminder.__doc__
    frequency, date_string, msg = args.split(' ', 2)
    periodicity = TYPES[frequency.lower()]
    date = datetime.strptime(date_string, '%d-%m')
    if add_reminder(chat_id, periodicity, date, msg):
        return "Reminder added correctly"
    else:
        return "There was a problem adding your reminder, try again!\n{}".format(reminder.__doc__)

# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Default answer for wrong commands """
    return "The command {} doesn't exists".format(command)
