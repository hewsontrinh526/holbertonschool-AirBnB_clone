#!/usr/bin/python3
""" Command interpreter project console """
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ Holberton Command prompt to access models' data"""
    prompt = '(hbnb)'

    # Quit command method
    def do_quit(self, arg):
        """ Quit command to exit program"""
        return True

    # EOF command method <Ctrl + D to exit>
    def do_EOF(self, arg):
        """ EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
