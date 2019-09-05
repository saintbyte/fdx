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
        pass