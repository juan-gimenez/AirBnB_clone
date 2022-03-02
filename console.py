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
        return True

    def do_EOF(self, arg):
        """
        EOF method which raises End Of File
        """
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
        flag = 0
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
                    if len(args) == 1:
                        print("** instance id missing **")
                        return
                    else:
                        if args[1] == objAndIdList[1]:
                            flag = 1
                            print(jsLoaded[obj])
                            return
            if flag == 0:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        jsLoaded = storage.all()
        flag = 0
        if arg == "":
            print("** class name missing **")
            return
        else:
            for obj in jsLoaded.keys():
                # making a list with the class name of the object and their id
                objAndIdList = obj.split('.')
                if args[0] not in self.classList:
                    print("** class doesn't exist **")
                    return
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                        return
                    else:
                        if objAndIdList[1] == args[1]:
                            flag = 1
                            jsLoaded.pop(obj)
                            storage.save()
                            return
            if flag == 0:
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
        args = arg.split()
        flag = 0
        if arg == "":
            print("** class name missing **")
            return
        for obj in jsLoaded:
            # making a list with the class name of the object and their id
            objAndIdList = obj.split('.')
            if args[0] not in self.classList:
                print("** class doesn't exist **")
                return
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                    return
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                        return
                    else:
                        if len(args) == 3:
                            print("** value missing **")
                            return
                        else:
                            if objAndIdList[1] == args[1]:
                                flag = 1
                                setattr(jsLoaded[obj], args[2],
                                        args[3].strip('"'))
                                storage.save()
                                return
        if flag == 0:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
