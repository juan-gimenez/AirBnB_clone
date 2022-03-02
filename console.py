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
    classList = ["BaseModel", "City", "State", "Place", "Review", "User", "Amenity"]

    def emptyline(self):
        """overwritted method to avoid a message if the command line is empty"""
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
        elif arg in self.classList:
            new = eval(arg)()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints str of an instance Ex: $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        jsLoaded = storage.all()
        flag = 0
        if arg == "":
            print("** class name missing **")
        else:
            print(f'jsLoaded es: \n{jsLoaded}')
            for obj in jsLoaded:
                #making a list with the class name of the object and their id
                objAndIdList = obj.split('.')
                if args[0] not in self.classList:
                    print("** class doesn't exist **")
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        if args[1] == objAndIdList[1]:
                            flag = 1
                            print(jsLoaded[obj])
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        jsLoaded = storage.all()
        flag = 0
        if arg == "":
            print("** class name missing **")
        else:
            for obj in jsLoaded.keys():
                #making a list with the class name of the object and their id
                objAndIdList = obj.split('.')
                if args[0] not in self.classList:
                    print("** class doesn't exist **")
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        if objAndIdList[1] == args[1]:
                            flag = 1
                            jsLoaded.pop(obj)
                            storage.save()
                            return
            if flag == 0:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representation of all instances
        """
        jsLoaded = storage.all()
        flag = 0
        i = 0
        for obj in jsLoaded:
            #making a list with class name of the object and their id
            objAndIdList = obj.split('.')
            if arg != "" and arg not in self.classList:
                print("** class doesn't exist **")
                return
            elif arg != "" and arg == objAndIdList[0]:
                if flag == 0:
                    print("[\"", end='')
                    flag = 1
                print(jsLoaded[obj],end='')
                if flag == 1 and i < len(jsLoaded) - 1:
                    print(", ", end='')
                i += 1
            if arg == "":
                if flag == 0:
                    print("[\"", end='')
                    flag = 1
                print(jsLoaded[obj],end='')
                if flag == 1 and i < len(jsLoaded) - 1:
                    print(", ", end='')
                i += 1
        print("\"]")

    def do_update(self, arg):
        """
        Updates an specific instance by adding or updating attribute
        """
        jsLoaded = storage.all()
        args = arg.split()
        flag = 0
        if arg == "":
            print("** class name missing **")
        for obj in jsLoaded:
            #making a list with the class name of the object and their id
            objAndIdList = obj.split('.')
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
                            if objAndIdList[1] == args[1]:
                                flag = 1
                                setattr(jsLoaded[obj], args[2], args[3].strip('"'))
                                storage.save()
        if flag == 0:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
