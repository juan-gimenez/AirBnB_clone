#!/usr/bin/python3
"""
console.py module which contains the console
"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from datetime import datetime
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand contains the commands of our interpeter
    """

    prompt = '(hbnb) '
    classList = ["BaseModel", "City", "State", "Place",
                 "Review", "User", "Amenity"]

    def emptyline(self):
        """
        overwritted method to avoid a message if the
        command line is empty
        """
        pass

    def do_quit(self, arg):
        """
        quit method which raises End Of File
        """
        print("")
        return True

    def do_EOF(self, arg):
        """
        EOF method which raises End Of File
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Creates instances of BaseModel, saves into a JSON file and prints id
        """
        if arg == "":
            print("** class name missing **")
            return
        elif arg in self.classList:
            new = eval(arg)()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """
        Prints str of an instance Ex: $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        jsLoaded = storage.all()
        if arg == "":
            print("** class name missing **")
            return
        else:
            # making a list with the class name of the object and their id
            if args[0] not in self.classList:
                print("** class doesn't exist **")
                return
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                else:
                    try:
                        print(jsLoaded[f'{args[0]}.{args[1]}'])
                        return
                    except Exception:
                        print("** no instance found **")
                        return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        jsLoaded = storage.all()
        if arg == "":
            print("** class name missing **")
            return
        else:
            # making a list with the class name of the object and their id
            if args[0] not in self.classList:
                print("** class doesn't exist **")
                return
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                else:
                    try:
                        jsLoaded.pop(f'{args[0]}.{args[1]}')
                        storage.save()
                        return
                    except Exception:
                        print("** no instance found **")
                        return

    def do_all(self, arg):
        """
        Prints string representation of all instances
        """
        jsLoaded = storage.all()
        toPrint = []
        for obj in jsLoaded:
            # making a list with class name of the object and their id
            objAndIdList = obj.split('.')
            if arg != "" and arg not in self.classList:
                print("** class doesn't exist **")
                return
            elif arg != "" and arg == objAndIdList[0]:
                toPrint.append(str(jsLoaded[obj]))
            if arg == "":
                toPrint.append(str(jsLoaded[obj]))
        print(toPrint)

    def do_update(self, arg):
        """
        Updates an specific instance by adding or updating attribute
        """
        jsLoaded = storage.all()
        flag = 0
        if '{' not in arg:
            args = arg.split()
            if arg == "":
                return
            if args[0] not in self.classList:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(args) == 3:
                            print("** value missing **")
                        else:
                            try:
                                check = args[3].replace(".", "", 1)
                                args[3] = args[3].strip('"')
                                if check.isdigit():
                                    if '.' in args[3]:
                                        args[3] = float(args[3])
                                    else:
                                        args[3] = int(args[3])
                                if args[2] == "id":
                                    return
                                if args[2] == "created_at":
                                    return
                                if args[2] == "updated_at":
                                    return
                                key = f'{args[0]}.{args[1]}'
                                setattr(jsLoaded[key], args[2], args[3])
                                time = datetime.now()
                                setattr(jsLoaded[key], "updated_at", time)
                                storage.save()
                            except Exception:
                                print("** no instance found **")

        else:
            y = arg.split('{')
            z = "{" + y[1]
            kwargs = eval(z)
            args = y[0].split(' ')
            try:
                classId = f'{args[0]}.{args[1]}'
                for key in kwargs:
                    setattr(jsLoaded[classId], key, kwargs[key])
                setattr(jsLoaded[classId], "updated_at", datetime.now())
                storage.save()
            except Exception:
                print("** no instance found **")
            print(args)

    def do_count(self, arg):
        """
        count the cuantity of objects of a specific class
        """
        args = arg.split()
        jsLoaded = storage.all()
        i = 0
        if arg == "":
            print("** class name missing **")
            return
        else:
            for obj in jsLoaded:
                # making a list with the class name of the object and their id
                objAndIdList = obj.split('.')
                if args[0] not in self.classList:
                    print("** class doesn't exist **")
                    return
                else:
                    if args[0] == objAndIdList[0]:
                        i += 1
            print(i)

    def default(self, arg):
        """
        Method called on an input line when the command prefix
        is not recognized. If this method is not overridden,
        it prints an error message and returns.
        """
        Rarg = arg.strip(')')
        Rarg = Rarg.strip('(')
        Rarg = Rarg.replace("\"", ".")
        args = Rarg.split('.')
        try:

            # User.all()
            # User.count()
            try:
                eval(f'self.do_{args[1]}')(args[0])
            except Exception:
                try:
                    args[1] = args[1].strip('(')
                    if len(args) == 4:
                        print(f'len: {len(args)}')
                        eval(f'self.do_{args[1]}')(f'{args[0]} {args[2]}')
                    else:
                        Rarg = arg.split('.')
                        if len(Rarg) != 2:
                            return
                        Rarg[1] = Rarg[1].replace("(", ",")
                        Larg = Rarg[1].split(',')
                        Larg[0] = Larg[0].strip('"')
                        Larg[1] = Larg[1].strip(' ')
                        Larg[1] = Larg[1].strip('"')
                        Larg[2] = Larg[2].strip(' ')
                        Larg[2] = Larg[2].strip('"')
                        Larg[3] = Larg[3].strip(' ')
                        Larg[3] = Larg[3].strip(')')
                        pep8Plz = f'{Rarg[0]} {Larg[1]} {Larg[2]} {Larg[3]}'
                        eval(f'self.do_{Larg[0]}')(pep8Plz)
                except Exception:
                    y = arg.split('{')
                    z = y[1].strip(' ')
                    z = z.strip(')')
                    z = "{" + z
                    zLeft = y[0].replace("(", ".")
                    zLeft = zLeft.strip(' ')
                    zLeft = zLeft.strip(',')
                    zLeft = zLeft.split('.')
                    zLeft[2] = zLeft[2].strip('"')
                    eval(f'self.do_{zLeft[1]}')(f'{zLeft[0]} {zLeft[2]} {z}')
        except Exception as a:
            print(f'*** Unknown syntax: {arg}')
            print(a)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
