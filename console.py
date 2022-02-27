#!/usr/bin/python3
"""
console.py module which contains the console
"""

import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand contains the commands of our interpeter
    """

    prompt = '(hbnb) '

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
        elif arg == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints str of an instance Ex: $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        jsLoaded = storage.reload()
        if arg == "":
            print("** class name missing **")
        else:
            for obj in jsLoaded:
                #making a list with the class name of the object and their id
                objAndIdList = obj.split('.')
                if args[0] != objAndIdList[0]:
                    print("** class doesn't exist **")
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        flag = 0
                        for attr in jsLoaded[obj]:
                            if jsLoaded[obj][attr] == args[1]:
                                flag = 1
                                toPrint = BaseModel(**jsLoaded[obj])
                                print(toPrint)
            if flag == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        jsLoaded = storage.reload()
        if arg == "":
            print("** class name missing **")
        else:
            for obj in jsLoaded:
                #making a list with the class name of the object and their id
                objAndIdList = obj.split('.')
                if args[0] != objAndIdList[0]:
                    print("** class doesn't exist **")
                else:
                    if len(args) == 1:
                        print("** instance id missing **")
                    else:
                        flag = 0
                        for attr in jsLoaded[obj]:
                            if jsLoaded[obj][attr] == args[1]:
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
        jsLoaded = storage.reload()
        flag = 0
        for obj in jsLoaded:
            #making a list with class name of the object and their id
            objAndIdList = obj.split('.')
            if arg != "" and arg != objAndIdList[0]:
                print("** class doesn't exist **")
                return
            elif arg == objAndIdList[0]:
                toPrint = BaseModel(**jsLoaded[obj])
                print(f'["{toPrint}"]')
                return
            else:
                toPrint = BaseModel(**jsLoaded[obj])
                if flag == 0:
                    print("[\"",end='')
                    flag = 1
                print(toPrint,end='')
        print("\"]")

    def do_update(self, arg):
        """
        Updates an specific instance by adding or updating attribute
        """
        jsLoaded = storage.reload()
        args = arg.split()
        flag = 0
        if arg == "":
            print("** class name missing **")
        for obj in jsLoaded:
            #making a list with the class name of the object and their id
            objAndIdList = obj.split('.')
            if args[0] != objAndIdList[0]:
                print("** class doesn't exist **")
            else:
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    for attr in jsLoaded[obj]:
                        if len(args) == 2:
                            print("** attribute name missing **")
                        else:
                            if len(args) == 3:
                                print("** value missing **")
                            else:
                                if jsLoaded[obj][attr] == args[1]:
                                    flag = 1
                                    jsLoaded[obj][args[2]] = args[3].strip('"')
                                    storage.save()
                                    return

        if flag == 0:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
