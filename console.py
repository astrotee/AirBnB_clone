#!/usr/bin/python3
"""console entry point"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
import cmd
from models import storage

models_map = {"BaseModel": BaseModel,
              "User": User,
              "State": State,
              "Review": Review,
              "Place": Place,
              "City": City,
              "Amenity": Amenity
              }


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """create a new object of a model"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        model = args[0]
        if model in models_map:
            obj = models_map[model]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """show instange of a model using class name and instance id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        model = args[0]
        id = args[1]
        objects = storage.all()
        if model in models_map:
            if f"{model}.{id}" in objects:
                print(str(objects[f"{model}.{id}"]))
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """update an instange of a model using class name and instance id"""
        sargs = args.split()
        if len(sargs) == 0:
            print("** class name missing **")
            return
        elif len(sargs) == 1:
            print("** instance id missing **")
            return
        elif len(sargs) == 2:
            print("** attribute name missing **")
            return
        elif len(sargs) == 3:
            print("** value missing **")
            return
        if sargs[3].startswith('"'):
            start = args.find(sargs[3][1:])
            end = args.find('"', start)
            sargs[3] = args[start:end]
        sargs = sargs[:4]

        model, id, aname, avalue = sargs
        key = f"{model}.{id}"
        objects = storage.all()
        if model in models_map:
            if key in objects:
                obj = objects[key]
                d = obj.__dict__
                vtype = type(d[aname]) if aname in d else str
                d[aname] = vtype(avalue)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """show all instanges of a specific model or all models"""
        args = args.split()
        model = args[0] if len(args) > 0 else None
        objects = storage.all()
        if model is not None and model not in models_map:
            print("** class doesn't exist **")
            return
        plist = list()
        for k, v in objects.items():
            if model is None or k.startswith(model):
                plist.append(str(v))
        print(plist)

    def do_destroy(self, args):
        """remove instange of a model using class name and instance id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        model = args[0]
        id = args[1]
        objects = storage.all()
        if model in models_map:
            if f"{model}.{id}" in objects:
                storage.remove(model, id)
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, args):
        """exit cmd"""
        return True

    do_EOF = do_quit

    def emptyline(self) -> bool:
        """do nothing"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
