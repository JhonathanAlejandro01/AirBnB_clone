#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """class interactive console"""
    prompt = '(hbnb) '

    def do_quit(self, args):
        """command to exit the program, it's same as EOF'"""
        return True

    def do_EOF(self, args):
        """command to exit the program, it's same as quit"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
