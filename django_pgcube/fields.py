__author__ = 'sb'

from django.db import models


class CubeField(models.Field):
    description = 'Cube Postgres Field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def value_to_string(self, obj):
        return super().value_to_string(obj)

    def db_type_parameters(self, connection):
        return super().db_type_parameters(connection)

    def db_type(self, connection):
        if connection.settings_dict['ENGINE'] == 'django.db.backends.mysql':
            return 'varchar'
        elif connection.settings_dict['ENGINE'] == 'django.db.backends.sqlite3':
            return 'text'
        elif connection.settings_dict['ENGINE'] == 'django.contrib.gis.db.backends.postgis':
            return 'cube'
        elif connection.settings_dict['ENGINE'] == 'django.db.backends.postgresql':
            return 'cube'
        else:
            return 'text'

    def get_db_prep_value(self, value, connection, prepared=False):
        if isinstance(value, (list, tuple)):
            return [self.base_field.get_db_prep_value(i, connection, prepared=False) for i in value]
        return value

    def to_python(self, value):
        if isinstance(value, str):
            # Assume we're deserializing
            vals = json.loads(value)
            value = [self.base_field.to_python(val) for val in vals]
        return value