#!/usr/bin/python3
"""The console module
"""
import re
import sys
import cmd
import json
import models
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.base_model import BaseModel

classes_dict = {
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
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Handles end-of-file: EOF
        """
        return True

    def do_quit(self, line):
        """Quit command to exit program
        """
        return True

    def help_quit(self):
        """two arguments involved"""
        print('\n'.join(["Quit command to exit the program"]))


    def emptyline(self):
        """Does nothing when empty line is entered in response to the prompt
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        """
        if line:
            try:
                temp_class = globals().get(line, None)
                tmp = temp_class()
                tmp.save()
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id.
        """
        tmp = line.split()
        if len(tmp) < 1:
            print("** class name missing **")
        elif tmp[0] not in classes_dict:
            print("** class doesn't exit **")
        elif len(tmp) < 2:
            print("** instance id missing **")
        else:
            new_string = "{}.{}".format(tmp[0], tmp[1])
            if new_string not in storage.all():
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        tmp = line.split()
        if len(tmp) < 1:
            print("** class name missing **")
        elif tmp[0] not in classes_dict:
            print("** class doesn't exit **")
        elif len(tmp) < 2:
            print("** instance id missing **")
        else:
            new_string = "{}.{}".format(tmp[0], tmp[1])
            if new_string not in storage.all().keys():
                print("** no instance found **")
            else:
                del(storage.all()[new_string])
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        str_list = []
        if not line:
            for key, val in storage.all().items():
                str_list.append(str(val))
            print(str_list)
        elif line not in classes_dict:
            print("** class doesn't exist **")
        else:
            for key, val in storage.all().items():
                if val.__class__.__name__ == line:
                    str_list.append(str(val))
            print(str_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        tmp = line.split()
        if len(tmp) < 1:
            print("** class name missing **")
        elif tmp[0] not in classes_dict:
            print("** class doesn't exit **")
        elif len(tmp) < 2:
            print("** instance id missing **")
        else:
            new_string = "{}.{}".format(tmp[0], tmp[1])
            if new_string not in storage.all().keys():
                print("** no instance found **")
            elif len(tmp) < 3:
                print("** attribute name missing **")
            elif len(tmp) < 4:
                print("** value missing **")
            else:
                setattr(storage.all()[new_string], tmp[2], tmp[3])
                storage.save()

    def do_count(self, line):
        """Retrieves the number of instances of a class
        """
        tmp = globals().get(line, None)
        if tmp is None:
            print("** class doesn't exist **")
            return
        class_count = 0
        for val in storage.all().values():
            if val.__class__.__name__ == line:
                class_count += 1
        print(class_count)

    def precmd(self, line):
        """Checks for specified input format
        and groups them together to create a proper commandline
        """
        if line is None:
            return

        cmd_pattern = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        param_pattern = r'^"([^"]+)"(?:,\s*'
        r'(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?'

        tmp = re.match(cmd_pattern, line)
        if not tmp:
            super().precmd(line)
            return
        tmp_name, tmp_method, tmp_params = tmp.groups()
        tmp = re.match(param_pattern, tmp_params)
        tmp_params = [i for i in tmp.groups() if i] if tmp else []

        command = " ".join([tmp_name] + tmp_params)

        if tmp_method == 'show':
            return self.do_show(command)

        if tmp_method == 'destroy':
            return self.do_destroy(command)

        if tmp_method == 'all':
            return self.do_all(command)

        if tmp_method == 'update':
            return self.do_update(command)

        if tmp_method == 'count':
            return self.do_count(command)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
