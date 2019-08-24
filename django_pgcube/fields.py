__author__ = 'sb'

from django.db import models


class CubeField(models.Field):
    description = 'Cube Postgres Field'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def value_to_string(self, obj):
        return super().value_to_string(obj)

    def db_type_parameters(self, connection):
        return None

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

    #def get_db_prep_value(self, value, connection, prepared=True):


    def get_db_prep_save(self, value, connection):
        if isinstance(value, (str)):
            s = value
        if isinstance(value, (list, tuple)):
            s = ','.join(str(si) for si in value)
        if self.is_engine_support(connection):
            return 'CUBE(array[ %s ])' % s
        else:
            return s

    def to_python(self, value):
        if isinstance(value, str):
            # Assume we're deserializing
            pass
        return value
