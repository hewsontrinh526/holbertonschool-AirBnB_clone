#!/usr/bin/python3
""" Command interpreter project console """
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User

class HBNBCommand(cmd.Cmd):
    """ Holberton Command prompt to access models' data"""
    prompt = '(hbnb) '

    # Quit command method
    def do_quit(self, args):
        """ Quit command to exit program"""
        return True

    # EOF command method <Ctrl + D to exit>
    def do_EOF(self, args):
        """ EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty line + ENTER"""
        pass

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it to the JSON file and
        prints the id
        """
        argument_list = args.split()
        if len(argument_list) < 1:
            print("** class name missing **")
        elif argument_list[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        argument_list = args.split()
        if len(argument_list) == 0:
            print("** class name missing **")
        elif argument_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argument_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argument_list[0], argument_list[1])
            current_dict = storage.all()
            try:
                print(current_dict[key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """
        argument_list = args.split()
        if len(argument_list) == 0:
            print("** class name missing **")
        elif argument_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(argument_list) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(argument_list[0], argument_list[1])
            current_dict = storage.all()
            try:
                del current_dict[key]
                storage.all()
            except Exception:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances based or ot on the
        class name
        """
        argument_list = args[0].split()
        current_dict = storage.all()
        output_list = []

        if len(argument_list) == 0:
            for tup_object in current_dict.items():
                output_list.append(tup_object[1].__str__)
            print(output_list)
            return

        class_name = argument_list[0]

        if class_name != "BaseModel":
            print("** class doesn't exist **")
        else:
            for tup_object in current_dict.items():
                instance = tup_object[1]
                instance_class = str(instance.__class__.__name__)
                if instance_class == class_name:
                    output_list.append(instance.__str__())
            print(output_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
