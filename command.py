from random import choice
import os

TOKEN = str(os.environ['TOKEN'])
# Public commands

def start(sender_id, command):
    return "DeptoonReminder at your service"

# Auxiliary methods

def not_found(sender_id, command, *args):
    """ Default answer for wrong commands """
    return 'The command {} doesn"t exists'.format(command)
