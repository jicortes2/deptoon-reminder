from random import choice
from db import add_element
import os


TOKEN = str(os.environ['TOKEN'])
# Public commands

def start(sender_id, command):
    return "Deptoon Reminder at your service"

def reminder(chat_id, command, args):
    print(command)
    print(args)
    return command

# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Default answer for wrong commands """
    return "The command {} doesn't exists".format(command)
