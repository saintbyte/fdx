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
from fdx_indexer.models import *
import urllib.request

class Command(BaseCommand):
    help = '---'

    def handle(self, *args, **options):
        self.stdout.write('Start')
        for domain in indexedSite.objects.filter(is_indexed=False):
            #-------------------------------------------
            # Выясняем вообше по какому протоколу работает сайта
            domain_str = domain.domain.encode('idna')
            url = 'https://{}/'.format(domain_str)
            self.stdout.write(url)
            try:
                req = urllib.request.Request(url)
                response = urllib.request.urlopen(req)
            except Exception:
                e,v, tv = sys.exc_info()
                print(e)
                print(v)
                continue
            #response.url
            url = 'http://{}/'.format(domain_str)
            self.stdout.write(url)
            #-------------------------------------------
            # Грузим robots.txt
            #-------------------------------------------
            # Грузим sitemap.xml

        self.stdout.write('End')