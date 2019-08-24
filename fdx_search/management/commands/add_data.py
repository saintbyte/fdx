__author__ = 'sb'
from django.utils import timezone
import json
import csv
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.contrib.gis.geos import Point
import os
import sys
from django.db import connection

from fdx_search.models import *

class Command(BaseCommand):
    help = '---'

    def add_arguments(self, parser):
        parser.add_argument('--file', nargs='+', help="File for parse")

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Start'))
        #Clear
        Faces.objects.all().delete()
        Images.objects.all().delete()
        filename = str(options['file'][0])
        fh = open(filename, 'r')
        faces = False
        cursor = connection.cursor()
        mcnt = 0
        for line in fh:
            mcnt = mcnt + 1
            if mcnt % 1000 == 0:
                print(str(mcnt))
            line = line.strip()
            if line == '---':
                faces = False
                continue
            arr = line.split(';',3)
            if not faces:
                url = arr[0]
                alt = arr[1]
                ind = arr[2]
                url = url.replace('I/m/','')
                url = 'https://ru.wikipedia.org/wiki/Файл:'+url
                im = Images()
                im.page = None
                im.url = url
                im.alt = alt
                im.tagNum = 1
                im.save()
                faces = True
                continue
            location = arr[0]
            vec_low = arr[1]
            vec_high = arr[2]
            (top, right, bottom, left) = location.split(',')
            """
            f = Faces()
            f.image = im
            f.people = None
            f.top = int(top)
            f.right = int(right)
            f.bottom = int(bottom)
            f.left = int(left)
            f.type_of_metod = 1
            f.vec_low = vec_low
            f.vec_high = vec_high
            f.save()
            """
            query = """
              INSERT INTO "fdx_search_faces" ("image_id",
                "people_id", "top", "right", "bottom", "left", "type_of_metod", "vec_low", "vec_high")
                VALUES (%s, NULL, %s, %s, %s, %s, %s, CUBE(ARRAY[%s]), CUBE(ARRAY[%s])) RETURNING "fdx_search_faces"."id"
            """ % (im.pk, top, right, bottom, left, 1, vec_low, vec_high)
            #print(query)
            #Faces.objects.raw(query
            cursor.execute(query)
        fh.close()
        self.stdout.write(self.style.SUCCESS('End'))
