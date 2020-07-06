#!/usr/bin/python3
"""new class console"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User


class HBNBCommand(cmd.Cmd):
    """class interactive console"""
    prompt = '(hbnb) '

    dict_class = {'BaseModel': BaseModel, 'User': User}

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
        else:
            try:
                new_inst = eval(args[0] + '()')
                models.storage.save()
                print(new_inst.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, argv):
        """show intance id"""
        args = argv.split()
        objects = models.storage.all()
        if len(argv) == 0:
            print("** class name missing **")
        elif args[0] not in self.dict_class:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            name_intance = args[0] + "." + args[1]
            if name_intance in objects:
                print(objects[name_intance])
            else:
                print("** no instance found **")

    def do_destroy(self, argv):
        """delent intance select it """
        args = argv.split()
        objects = models.storage.all()
        if len(argv) == 0:
            print("** class name missing **")
        elif args[0] not in self.dict_class:
            print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        else:
            name_intance = args[0] + "." + args[1]
            if name_intance in objects.keys():
                objects.pop(name_intance, None)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, argv):
        """rints all string representation of all instances based """
        argvs = argv.split()
        new_list = []
        if len(argv) == 0:
            for value in models.storage.all().values():
                new_list.append(value.__str__())
            print(new_list)
            return
        elif argvs[0] not in self.dict_class:
            print("** class doesn't exist **")

        else:
            for key, value in models.storage.all().items():
                if argvs[0] in key:
                    new_list.append(models.storage.all()[key].__str__())
            print(new_list)

    def do_update(self, argv):
        """add attribute within an instance"""
        args = argv.split()
        if len(argv) == 0:
            print("** class name missing **")
        elif (args[0]) not in self.dict_class:
                print("** class doesn't exist **")
        elif len(argv) == 1:
            print("** instance id missing **")
        elif len(argv) == 2:
            print("** attribute name missing **")
        elif len(argv) == 3:
            print("** value missing **")
        elif len(argv) == 4:
            try:
                name_intance = args[0] + "." + args[1]
                setattr(models.storage.all()[name_intance], args[2], args[3])
                models.storage.save()
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
