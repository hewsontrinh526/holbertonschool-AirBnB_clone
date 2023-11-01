#!/usr/bin/python3
"""Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class_dict = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """ Override emptyline to do nothing\n"""
        pass

    def do_EOF(self, args):
        """Exits the program\n"""
        raise SystemExit

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it to a json\
file and prints the id\n"""
        if args == "" or args is None:
            print("** class name missing **")
        else:
            args_list = args.split(' ')
            if args_list[0] not in class_dict.keys():
                print("** class doesn't exist **")
            else:
                new_instance = class_dict[args_list[0]]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class\
 name and id\n """
        args_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif (len(args_list) < 2):
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            new_key = str(args_list[0]) + "." + str(args_list[1])
            for k, v in obj_dict.items():
                if k == new_key:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id (saves the \
changes into the JSON file). """
        args_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif (len(args_list) < 2):
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key_to_del = str(args_list[0]) + "." + str(args_list[1])
            for k, v in obj_dict.items():
                if k == key_to_del:
                    del obj_dict[k]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not\
on the class name(eg, all or all BaseModel)"""
        args_list = args.split(" ")
        obj_dict = storage.all()
        new_list = []
        if len(args) == 0:
            for value in obj_dict.values():
                new_list.append(value.__str__())
            print(new_list)
        elif args_list[0] in class_dict.keys():
            for value in obj_dict.values():
                if value.__class__.__name__ == args_list[0]:
                    new_list.append(value.__str__())
            print(new_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or\
updating attribute (saves the change into the JSON file) """
        args_list = args.split(" ")
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif len(args_list) == 2:
            print("** attribute name missing **")
        elif len(args_list) == 3:
            print("** value missing **")
        else:
            id_to_update = args_list[1]
            for value in obj_dict.values():
                if value.__class__.__name__ == args_list[0]:
                    if value.id == id_to_update:
                        setattr(value, args_list[2], args_list[3])
                        storage.save()
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
