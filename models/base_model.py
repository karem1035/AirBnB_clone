"""for generating UUIDs (Universally Unique Identifiers)."""
import uuid
import datetime


class BaseModel:
    """
    Base class for models with common attributes and methods.
    """

    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current timestamp.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary containing the attributes of the instance.
        """
        # Get the attribute dictionary
        obj_dict = self.__dict__.copy()
        # Add class name to the dictionary
        obj_dict['__class__'] = self.__class__.__name__
        # Convert datetime attributes to ISO 8601 format
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
