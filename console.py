#!/usr/bin/python3
"""this code is console which help the user to use the airbnb website"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command Processor"""
    classes = ["BaseModel"]

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
        class_name = line.split()[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return

        lines = line.split()
        if len(lines) < 2:
            print("** instance id missing **")
            return
        class_name = lines[0]
        instance_id = lines[1]
        if not instance_id:
            print("** instance id missing **")
            return

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        object_key = f"{class_name}.{instance_id}"
        objectFound = storage.all().get(object_key)
        if objectFound:
            print(objectFound)
        else:
            print("** no instance found **")
    def do_destroy(self, line):
        """eletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return

        lines = line.split()
        if len(lines) < 2:
            print("** instance id missing **")
            return
        class_name = lines[0]
        instance_id = lines[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        object_key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if object_key in objects:
            del objects[object_key]
            storage.save()
        else:
            print("** no instance found **")

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
        
        class_name = lines[0]
        class_id = lines[1]
        attribute_name = lines[2]
        attribute_value = lines[3].strip('"')
        
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        
        object_key = f"{class_name}.{class_id}"
        class_instance = eval(class_name)

        if not issubclass(class_instance, BaseModel):
            print("** class doesn't exist **")
            return
        
        objects = storage.all()
        if object_key not in objects:
            print("** no instance found **")
            return

        if len(lines) < 3:
            print("** attribute name missing **")
            return
        elif len(lines) < 4:
            print("** value missing **")
            return
        obj = objects[object_key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
