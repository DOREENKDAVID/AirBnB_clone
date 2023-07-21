#!/usr/bin/python3

"""An interactive console module"""

import cmd
import re
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter
    """
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        """ Handles end-of-file: EOF Exits console"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("Quiting!")
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ Does nothing when empty line is entered
        in response to the prompt """
        return False
        # OR
        # pass

    def do_create(self, line):
        """Creates a new instances of a class
        saves it (to the JSON file) and prints the id.
        """
        if line:
            try:
                temp_class = globals().get(line, None)
                tmp = temp_class()
                tmp.save()
                print(tmp.id)  # print the id
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        """
        tmp = line.split()    # split & assign to varia

        if len(tmp) < 1:
            print("** class name missing **")
        elif tmp[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(tmp) < 2:
            print("** instance id missing **")
        else:
            new_string = "{}.{}".format(tmp[0], tmp[1])
            if new_string not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[new_string])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        tmp = line.split()
        if len(tmp) < 1:
            print("** class name missing **")
        elif tmp[0] not in class_dict:
            print("** class doesn't exist **")
        elif len(tmp) < 2:
            print("** instance id missing **")
        else:
            new_string = "{}.{}".format(tmp[0], tmp[1])
            if new_string not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(new_string)
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name. """
        str_list = []
        if line == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            string = line.split(" ")
            if string[0] not in class_dict:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    klass = key.split(".")
                    if klass[0] == string[0]:
                        objects.append(str(value))
                print(str_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        tmp = line.split()
        if len(temp) < 1:
            print("** class name missing **")
            return
        elif tmp[0] not in class_dict:
            print("** class doesn't exist **")
            return
        elif len(tmp) < 2:
            print("** instance id missing **")
            return
        else:
            new_string = f"{arr[0]}.{arr[1]}"
            if new_string not in storage.all().keys():
                print("** no instance found **")
            elif len(tmp) < 3:
                print("** attribute name missing **")
                return
            elif len(tmp) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_string], tmp[2], tmp[3])
                storage.save()

    def do_count(self, line):
        """Retrieves the number of instances of a class"""
        temp = globals().get(line, None)
        if temp is None:
            print("** class doesn't exist **")
            return
        class_count = 0
        for val in storage.all().values():
            if val.__class__.__name__ == line:
                class_count += 1
        print(class_count)

    def default(self, line):
        """Checks for specified input format
        and groups them together to create a proper commandline
        """
        if line is None:
            return

        cmd_Pattern = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        param_Pattern = r'^"([^"]+)"(?:,\s*'
        r'(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?'
        tmp = re.match(cmd_Pattern, line)
        if not tmp:
            super().default(line)
            return
        tmpName, tmp_method, tmp_params = tmp.groups()
        tmp = re.match(param_Pattern, tmp_params)
        tmp_params = [item for item in tmp.groups() if item] if tmp else []

        command = " ".join([tmpName] + tmp_params)

        if tmp_method == 'all':
            return self.do_all(command)

        if tmp_method == 'count':
            return self.do_count(command)

        if tmp_method == 'show':
            return self.do_show(command)

        if tmp_method == 'destroy':
            return self.do_destroy(command)

        if tmp_method == 'update':
            return self.do_update(command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
