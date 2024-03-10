#!/usr/bin/python3
"""console entry point"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """exit cmd"""
        return True

    do_EOF = do_quit

    def emptyline(self) -> bool:
        """do nothing"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
