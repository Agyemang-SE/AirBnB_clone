#!/usr/bin/python3
"""Module for the HBNB command line interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the HBNB command line interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when empty line is entered."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file and
        prints the id
        """
        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split()
        class_name = arg_list[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(arg_list) < 2:
            print("** instance name missing **")
            return

        new_instance = classes[class_name]()
        for i in range(1, len(arg_list)):
            arg_pair = arg_list[i].split('=')
            if len(arg_pair) != 2:
                continue
            attr_name = arg_pair[0]
            attr_value = arg_pair[1]
            if hasattr(new_instance, attr_name):
                try:
                    attr_value = eval(attr_value)
                except:
                    pass
                setattr(new_instance, attr_name, attr_value)

        new_instance.save()
        print(new_instance.id)


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if not class_name in classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        all_objects[key].delete()
        storage.save()

     def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
        except:
            print("** class doesn't exist **")
            return
        objs = models.storage.all(cls)
        print([str(obj) for obj in objs])


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        arg_list = shlex.split(arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        class_name = arg_list[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        key = class_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return
        instance = models.storage.all()[key]
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return
        attribute = arg_list[2]
        if len(arg_list) == 3:
            print("** value missing **")
            return
        value = arg_list[3]
        if hasattr(instance, attribute):
            attr_type = type(getattr(instance, attribute))
            value = attr_type(value)
        setattr(instance, attribute, value)
        instance.save()

   if __name__ == '__main__':
    HBNBCommand().cmdloop()

