__author__ = 'sb'

import os
from django.core.files.storage import FileSystemStorage

RANDOM_FILENAME_LENGTH = 60


class Md5FileSystemStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if max_length and len(name) > max_length:
            raise(Exception("name's length is greater than max_length"))
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(Md5FileSystemStorage, self)._save(name, content)

