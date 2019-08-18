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

    def is_engine_support(self, connection):
        if connection.settings_dict['ENGINE'] in ['django.contrib.gis.db.backends.postgis',
                                                  'django.db.backends.postgresql',
                                                  'django.db.backends.postgresql_psycopg2']:
            return True

        else:
            # 'django.db.backends.mysql' 'django.db.backends.sqlite3'
            return False
    def db_type(self, connection):
        if self.is_engine_support(connection):
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