#!/usr/bin/python3
"""class BaseModel that defines all
common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel:
    """
    we are going to define all common attribute and methods
    those are

    public instance attributes:-

    id: assign a unique id by using uuid.uuid4() for basemodel
    created_at: current datetime when an instance created
    updated_at: current datetime when an instance is created and updatd

    public instance:-

    save(self): updates the public instance attribute
    updated_at with the current datetime

    to_dict(self): returns a dictionary containing
    all keys/values of __dict__ of the instance:
    """

    def __init__(self, *args, **kwargs):
        """ this is constructor for id and datetime"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            """
            Updates instance attributes based on the arguments.

            Args:
                kwargs (dict): Keyword arguments of the instance attributes.

            Description:
                - iterates over the provided keyword arguments
                - updates instance attributes accordingly
                - If the keyword argument is not '__class__',
                - checks if the key is 'created_at' or 'updated_at'.
                - converts the string to a datetime object.
            """
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            from models import storage
            storage.new(self)

    def __str__(self):
        """print class name, id and dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        """this method update the time of save"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """this code return dictionary containg all but it will add class"""
        instance_dict = self.__dict__.copy()
        instance_dict.update({'__class__': self.__class__.__name__})
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
