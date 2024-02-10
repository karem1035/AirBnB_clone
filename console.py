#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Processor"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Quit with EOF CTRL+D"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """dp nothing if enter command is given"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it and prints the id"""
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return

        lines = line.split()
        try:
            class_name = lines[0]
            instance_id = lines[1]
        except IndexError:
            print("** instance id missing **")
            return

        try:
            object_key = f"{class_name}.{instance_id}"
            objectFound = storage.all().get(object_key)
            if objectFound:
                print(objectFound)
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """eletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        lines = line.split()
        try:
            class_name = lines[0]
            instance_id = lines[1]
        except IndexError:
            print("** instance id missing **")
            return

        try:
            object_key = f"{class_name}.{instance_id}"
            objects = storage.all()
            if object_key in objects:
                del objects[object_key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances based"""
        try:
            if not line:
                objects = storage.all().values()
            else:
                class_name = line.strip()
                class_instance = eval(class_name)
                if not issubclass(class_instance, BaseModel):
                    raise NameError
                objects = [str(obj) for obj in storage.all().values()
                           if type(obj).__name__ == class_name]
            print(objects)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""
        if not line:
            print("** class name missing **")
            return
        lines = line.split()
        if len(lines) < 2:
            print("** instance id missing **")
            return
        try:
            class_name = lines[0]
            class_id = lines[1]
            object_key = f"{class_name}.{class_id}"
            class_instance = eval(class_name)

            if not issubclass(class_instance, BaseModel):
                print("** class doesn't exist **")
                return

            objects = storage.all()
            if object_key not in objects:
                print("** no instance found **")
                return

            attribute_name = lines[2]
            if len(lines) < 3:
                print("** attribute name missing **")
                return

            attribute_value = lines[3]
            if len(lines) < 4:
                print("** value missing **")
                return
            obj = objects[object_key]
            setattr(obj, attribute_name, attribute_value)
            obj.save()
        except NameError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
