#!/usr/bin/python3

"""Make the shell interactive"""

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

hbnb_class = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)  '

    def EOF_cls(self, input):
        """Close console"""
        print("")
        return True

    def quit_cls(self, input):
        """The command to exit the console"""
        print("Thanks and Good-Bye!")
        return True

    def hquit_cls(self):
        """helps to quit if 2 args are passed"""
        print('\n'.join(["The command to exit the console"]))

    def blank_cmd(self):
        """ emptyline - reruns the last command"""
        return False

    def create_cls(self, input):
        """This will create the new class"""
        if input:
            try:
                new_clss = globals().get(input, None)
                obj = new_clss()
                obj.save()
                print(obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def view_inst(self, input):
        """view instance details: print class name and id"""
        split_str = input.split()

        if len(split_str) < 1:
            print("** class name missing **")
        elif split_str[0] not in hbnb_class:
            print("** class doesn't exist **")
        elif len(split_str) < 2:
            print("** instance id missing **")
        else:
            str_uptd = f"{split_str[0]}.{split_str[1]}"
            if str_uptd not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[str_uptd])

    def del_inst(self, input):
        """Delete instance details: use class name and id"""
        split_str = input.split()
        if len(split_str) < 1:
            print("** class name missing **")
        elif split_str[0] not in hbnb_class:
            print("** class doesn't exist **")
        elif len(split_str) < 2:
            print("** instance id missing **")
        else:
            str_uptd = f"{split_str[0]}.{split_str[1]}"
            if str_uptd not in storage.all().keys():
                print("** no instance found **")
            else:
                storage.all().pop(str_uptd)
                storage.save()

    def print_inst(self, input):
        """This will print all instances"""
        all_inst = []
        if input == "":
            print([str(value) for key, value in storage.all().items()])
        else:
            input_str = input.split(" ")
            if input_str[0] not in hbnb_class:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    clas = key.split(".")
                    if clas[0] == input_str[0]:
                        all_inst.append(str(value))
                print(all_inst)

    def update_cls(self, input):
        """Update a class: modify the instances"""
        split_str = input.split()
        if len(split_str) < 1:
            print("** class name missing **")
            return
        elif split_str[0] not in hbnb_class:
            print("** class doesn't exist **")
            return
        elif len(split_str) < 2:
            print("** instance id missing **")
            return
        else:
            str_uptd = f"{split_str[0]}.{split_str[1]}"
            if str_uptd not in storage.all().keys():
                print("** no instance found **")
            elif len(split_str) < 3:
                print("** attribute name missing **")
                return
            elif len(split_str) < 4:
                print("** value missing **")
                return
            else:
                setattr(storage.all()[str_uptd], split_str[2], split_str[3])
                storage.save()

    def count_cls(self, input):
        """This counts all class instances"""
        all_class = globals().get(input, None)
        if all_class is None:
            print("** class doesn't exist **")
            return
        inst_counter = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == input:
                inst_counter += 1
        print(inst_counter)

    def default_cls(self, input):
        """Handles the default: unrecognized input command"""
        if input is None:
            return

        command_regex = r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        params_regex = r"""^"([^"]+)"(?:,\s*(?:"([^"]+)
        "|(\{[^}]+\}))(?:,\s*(?:"[^"]+"))?)?"""
        c_match = re.match(command_regex, input)
        if not c_match:
            super().default(input)
            return
        cmdIN, method, paramIN = c_match.groups()
        p_match = re.match(params_regex, paramIN)
        param_ext =
        [item for item in p_match.groups() if item] if p_match else []

        cmd = " ".join([cmdIN] + param_ext)

        if method == 'all':
            return self.print_inst(cmd)

        if method == 'count':
            return self.count_cls(cmd)

        if method == 'show':
            return self.view_inst(cmd)

        if method == 'destroy':
            return self.del_inst(cmd)

        if method == 'update':
            return self.update_cls(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
