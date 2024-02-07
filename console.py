#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command Processor"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit with EOF CTRL+D"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
