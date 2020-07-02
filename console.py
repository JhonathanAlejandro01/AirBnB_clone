#!/usr/bin/python3
"""new class console"""
import cmd
from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    """class interactive console"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """command to exit the program, it's same as EOF'"""
        return True

    def do_EOF(self, args):
        """command to exit the program, it's same as quit"""
        return True

    def emptyline(self):
        """ empty line + ENTER """
        pass

    def do_create(self, argv):
        """create new intance"""
        args = argv.split()
        if len(argv) == 0:
            print("** class name missing **")
        try:
            new_inst = eval(args[0] + '()')
            models.storage.save()
            print(new_inst.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, argv):
        """show intance id"""
        argv = argv.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            try:
                name_intance = argv[0] + "." + argv[1]
                print(models.storage.all()[name_intance])
            except:
                print("** no instance found **")

    def do_destroy(self, argv):
        """delent intance select it """
        argv = argv.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            try:
                name_intance = argv[0] + "." + argv[1]
                del models.storage.all()[name_intance]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_all(self, argv):
        """rints all string representation of all instances based """
        argv = argv.split()
        new_list = []
        if len(argv) == 0 or argv[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            name_intance = argv[0]
            for key, value in models.storage.all().items():
                if argv[0] in key:
                    new_list.append(models.storage.all()[key].__str__())
            print(new_list)

    def do_update(self, argv):
        """add attribute within an instance"""
        argv = argv.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif argv[0] != 'BaseModel':
                print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        elif len(argv) == 4:
            try:
                name_intance = argv[0] + "." + argv[1]
                setattr(models.storage.all()[name_intance], argv[2], argv[3])
                models.storage.save()
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
