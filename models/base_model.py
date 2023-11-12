#!/usr/bin/pyhon3
"""
Parent class that will in_herit attributes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """D_fines all _common _attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """initializes all _attributes _associated
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns _class _name, _id and _attribute _dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {k: v for (k, v) in self.__dict__.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """updates last time_updated
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """_creates a new _dictionary, adding a key and _returning
        datetime in string format
        """
        new_dictionary = {}

        for key, values in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                new_dictionary[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dictionary[key] = values
        new_dictionary['__class__'] = self.__class__.__name__

        return new_dictionary
