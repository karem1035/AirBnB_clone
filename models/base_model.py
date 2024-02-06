#!/usr/bin/python3
"""class BaseModel that defines all common
attributes/methods for other classes"""
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

    def __init__(self):
        """ this is constructor for id and datetime"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """print class name, id and dictionary"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """this method update the time of save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """this code return dictionary containg all but it will add cla"""
        instance_dict = self.__dict__
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
